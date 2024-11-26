from src.data_preprocessing.preprocess import preprocess_csv
from src.data_preprocessing.embeddings import generate_embeddings, upload_embeddings
import json

raw_filepath = "data/bdd.csv"
processed_filepath = "data/preprocessed.csv"

if __name__ == "__main__":
	preprocess_csv(raw_filepath, processed_filepath)
	embeds = generate_embeddings(processed_filepath)
	upload_embeddings(
		embeddings=embeds
	)