import os
import json
import pandas as pd
from dotenv import load_dotenv

import logging

from tqdm import tqdm

from src.pinecone.init import create_db
from src.pinecone.upsert import upsert_vectors
from src.data_preprocessing.preprocess import clean_text

from langchain_openai import AzureOpenAIEmbeddings

load_dotenv()


def generate_embeddings(input_csv):
	df = pd.read_csv(input_csv)
	answers = df["answers"].tolist()

	embeddings_function = AzureOpenAIEmbeddings(
		model='text-embedding-ada-002',
		chunk_size=512
	)

	embeddings = []
	for idx, (answers) in enumerate(
			tqdm(
				answers,
				total=len(answers),
				desc="Embedding Progress"
			)
	):
		try:
			lines = answers.split('\n')
			for i in range(len(lines)):
				line_embedding = embeddings_function.embed_query(clean_text(lines[i]))

				embeddings.append((
					f"answer_{idx}_line_{i}",
					line_embedding,
					{
						"answer": df["answers"].iloc[idx],
						"line": lines[i],
						"type": "answer",
						"text": df['domain'].iloc[idx]
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


def upload_embeddings_step(embeds):
	temp = []
	i = 0
	for embed in tqdm(embeds, 'Upload embeds'):
		if i != 10:
			temp.append(embed)
			i += 1
		else:
			upload_embeddings(
				temp
			)
			temp = []
			i = 0
