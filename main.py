from src.data_preprocessing.preprocess import preprocess_csv
from src.data_preprocessing.embeddings import generate_embeddings, upload_embeddings, upload_embeddings_step
from src.data_preprocessing.docx import chunk_doc
import json

raw_filepath = "data/bdd.csv"
processed_filepath = "data/preprocessed.csv"

if __name__ == "__main__":
	# preprocess_csv(raw_filepath, processed_filepath)
	# embeds = generate_embeddings(processed_filepath)
	# upload_embeddings(
	# 	embeddings=embeds
	# )

	embeds = []

	# for attr, value in text.items():
	# 	print(attr, value)
	# embeds = chunk_doc()
	with open('doc-embeds.json') as f:
		data = json.load(f)
		for t in data:
			embeds.append(tuple(t))
      
	upload_embeddings_step(embeds=embeds)
	# upload_embeddings(
	# 	embeddings=embeds_1
	# )
