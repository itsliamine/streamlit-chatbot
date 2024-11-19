import os
import time
from dotenv import load_dotenv
from src.pinecone.init import pinecone_init

def upsert_vectors(index_name, embeddings):
	pc = pinecone_init()
	index = pc.Index(index_name)
 
	index.upsert(
		vectors=embeddings
	)

	print("Vectors uploaded, waiting for indexing...")
	time.sleep(10)
	print(index.describe_index_stats())