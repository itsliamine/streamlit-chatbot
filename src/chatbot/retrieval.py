import os
from src.chatbot.prompt import initial_prompt, refine_prompt

from langchain.memory import ConversationBufferMemory

from langchain_community.llms import AzureOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from src.pinecone.init import pinecone_init
from langchain_pinecone import Pinecone
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever

from typing import Optional

import logging

from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.llms import AzureOpenAI
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_pinecone import Pinecone

from src.chatbot.prompt import prompt_template
from src.pinecone.init import pinecone_init

load_dotenv()


def retrieve():

	index = pinecone_init("law-test")

	embeddings_function = AzureOpenAIEmbeddings(
		model='text-embedding-ada-002',
	)

	vector_store = Pinecone(
		index,
		embeddings_function,
		"text",
	)

	try:
		llm = AzureChatOpenAI(
			temperature=0,
			azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
			openai_api_key=os.getenv('AZURE_OPENAI_API_KEY'),
			azure_deployment=os.getenv('LLM_DEPLOYMENT'),
			max_retries=3,
			request_timeout=30
		)
	except Exception as e:
		logging.error(f"Failed to initialize LLM: {str(e)}")
		raise

	compressor = LLMChainExtractor.from_llm(llm)

	retriever = vector_store.as_retriever(
		search_kwargs={
			"k": 10,
		}
	)

	compression_retriever = ContextualCompressionRetriever(
		base_compressor=compressor,
		base_retriever=retriever
	)

	memory = ConversationBufferMemory(
		memory_key="chat_history",
		input_key="question",
		output_key="answer",
		return_messages=True
	)

	qa = RetrievalQAWithSourcesChain.from_chain_type(
		llm=llm,
		chain_type="stuff",
		retriever=compression_retriever,
		chain_type_kwargs={
			"question_prompt": initial_prompt,
			"memory": memory,
			"document_variable_name": "context_str",
		},
		return_source_documents=True
	)

	return qa
