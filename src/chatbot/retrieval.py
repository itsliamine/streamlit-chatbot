from src.chatbot.prompt import initial_prompt

from langchain.memory import ConversationBufferMemory

from langchain_community.llms import AzureOpenAI
from langchain.chains import ConversationalRetrievalChain, LLMChain
from src.pinecone.init import pinecone_init
from langchain_pinecone import Pinecone
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever

from typing import Optional

import logging

from dotenv import load_dotenv
import os

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

	retriever = vector_store.as_retriever(
		search_kwargs={
			"k": 10,
		}
	)

	memory = ConversationBufferMemory(
		memory_key="chat_history",
		input_key="question",
		output_key="answer",
		return_messages=True,
		human_prefix="User",
		ai_prefix="Assistant"
	)


	qa = ConversationalRetrievalChain.from_llm(
		llm=llm,
		retriever=retriever,
		memory=memory,
		combine_docs_chain_kwargs={
			'prompt': initial_prompt
		}
	)

	return qa
