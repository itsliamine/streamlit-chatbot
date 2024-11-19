import os
import json
import pandas as pd
from dotenv import load_dotenv

from src.pinecone.init import create_db
from src.pinecone.upsert import upsert_vectors

from langchain.embeddings import OpenAIEmbeddings

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def generate_embeddings(input_csv):
	df = pd.read_csv(input_csv)
	text_data = df["Réponse écrite de DP"].tolist()
 
	embeddings_function = OpenAIEmbeddings(
		model="text-embedding-3-small"
	)
 
	embeddings = []
	for idx, text in enumerate(text_data):
		embedding = embeddings_function.embed_query(text)
		embeddings.append((str(idx), embedding, {"text": text}))

	with open('embeddings.json', 'w') as f:
		json.dump(embeddings, f)

	return embeddings
	
	
def upload_embeddings(embeddings):
	index_name = "law-test"
 
	create_db(
		index_name=index_name,
		dimension=len(embeddings[0][1])
	)
 
	upsert_vectors(
		index_name=index_name, 
		embeddings=embeddings
	)
