import os

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
        model="text-embedding-ada-002",
    )

    vector_store = Pinecone(
        index,
        embeddings_function,
        "text",
    )

    llm: AzureOpenAI = AzureChatOpenAI(
        temperature=0,
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_deployment=os.getenv("LLM_DEPLOYMENT"),
        top_p=0.9,
    )

    qa: RetrievalQA = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(
            search_kwargs={
                "k": 3,
            }
        ),
        chain_type_kwargs={"prompt": prompt_template},
    )

    return qa
