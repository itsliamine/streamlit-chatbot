import os
import time
import pinecone
from pinecone import ServerlessSpec, Pinecone
from dotenv import load_dotenv

load_dotenv()

def pinecone_init():
	pc = Pinecone(os.getenv("PINECONE_API_KEY"))
	return pc

def create_db(index_name, dimension):
	pc = pinecone_init()
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