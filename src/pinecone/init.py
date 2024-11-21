import os
import time
import pinecone
from pinecone import ServerlessSpec, Pinecone
from dotenv import load_dotenv

load_dotenv()

def pinecone_init(index_name):
	pc = Pinecone(os.getenv("PINECONE_API_KEY"))
	index = pc.Index(index_name)
	return index

def create_db(index_name, dimension):
	pc = Pinecone(os.getenv("PINECONE_API_KEY"))
	if index_name not in pc.list_indexes().names():
		pc.create_index(
			index_name,
			dimension=dimension,
			spec=ServerlessSpec(
				cloud="aws",
				region="us-east-1"
			)
		)
		
	while not pc.describe_index(index_name).status['ready']:
		time.sleep(1)
  
	print("Pinecone database initialized")