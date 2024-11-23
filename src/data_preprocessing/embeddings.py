import os
import json
import pandas as pd
from dotenv import load_dotenv

import logging

from tqdm import tqdm

from src.pinecone.init import create_db
from src.pinecone.upsert import upsert_vectors

from langchain_openai import AzureOpenAIEmbeddings

load_dotenv()


def generate_embeddings(input_csv):
	df = pd.read_csv(input_csv)
	answers_tokens = df["answers_tokens"].tolist()

	embeddings_function = AzureOpenAIEmbeddings(
		model='text-embedding-ada-002',
		chunk_size=512
	)

	embeddings = []
	for idx, (answer_tokens) in enumerate(
		tqdm(
			answers_tokens,
			total=len(answers_tokens),
			desc="Embedding Progress"
		)
	):
		try:
			token_embedding = embeddings_function.embed_query(" ".join(answer_tokens))
			
			embeddings.append((
				f"a_{idx}",
				token_embedding,
				{
					"text": df["answers"].iloc[idx],
					"tokens": answer_tokens,
					"type": "answer",
					"pair_id": idx
				}
			))

		except Exception as e:
			logging.error(f"Error embedding row {idx}: {str(e)}")
			continue

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
