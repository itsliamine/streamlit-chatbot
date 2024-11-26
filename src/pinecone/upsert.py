import os
import time
import logging
from dotenv import load_dotenv
from src.pinecone.init import pinecone_init

def upsert_vectors(index_name, embeddings):
	index = pinecone_init(index_name)

	logging.info('Upserting vectors...')
 
	index.upsert(
		vectors=embeddings
	)

	logging.info("Vectors uploaded, waiting for indexing...")
	time.sleep(10)
	print(index.describe_index_stats())