from src.data_preprocessing.preprocess import preprocess_csv, clean_text
from src.data_preprocessing.embeddings import generate_embeddings, upload_embeddings, upload_embeddings_step
import json
import pandas as pd

raw_filepath = "data/bdd.csv"
processed_filepath = "data/preprocessed.csv"

if __name__ == "__main__":
	preprocess_csv(
		raw_filepath,
		processed_filepath,
		drop_columns=[
			"Résumé bref de la demande",
			"Situation de handicap",
			"Action faite",	
			"Commentaires",
			"Lien avec le Memo"
		]
	)

	# embeds = generate_embeddings(processed_filepath)
	embeds = []
	with open('embeddings.json') as f:
		data = json.load(f)
		for t in data:
			embeds.append(tuple(t))

	upload_embeddings_step(
		embeds=embeds,
		step=200
	)
