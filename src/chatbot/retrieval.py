from src.chatbot.prompt import prompt_template

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chains import RetrievalQA
from src.pinecone.init import pinecone_init
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings

def retrieve():
	pc = pinecone_init()
	index = pc.Index("law-test")

	embeddings_function = OpenAIEmbeddings(
		model="text-embedding-3-small"
	)

	vector_store = Pinecone(
		index, 
		embeddings_function.embed_query, 
		"text"
	)
 
	llm: OpenAI = OpenAI(
		temperature=0,
	)

	qa: RetrievalQA = RetrievalQA.from_chain_type(
		llm=llm,
		chain_type="stuff", 
		retriever=vector_store.as_retriever(),
  		chain_type_kwargs={
			"prompt": prompt_template
		}
	)
 
	return qa