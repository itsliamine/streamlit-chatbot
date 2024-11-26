import pandas as pd
import re
import unicodedata
from typing import List
import logging

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

logging.getLogger('nltk').setLevel(logging.ERROR)

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text: str) -> str:
	if pd.isnull(text):
		return ""

	text = re.sub(r"[^a-zA-Z0-9\sÀ-ÖØ-öø-ÿ]", "", text)
	text = re.sub(r'[^\w\s.,?!-]', '', text)
	text = re.sub(r"\s+", " ", text).strip()
	return text


def preprocess_csv(
	file_path: str,
	output_path: str,
	drop_columns: List[str] = None
) -> None:
	
	try:
		df = pd.read_csv(file_path)
		df.columns = df.columns.str.strip()
		df.set_index("Numéro de dossier", inplace=True)

		if drop_columns:
			df.drop(columns=[col for col in drop_columns if col in df.columns], inplace=True)

		df.rename(
			columns={
				"Réponse écrite de DP": "answers",
				"Domaine de la question de droit" : "domain"
			},
			inplace=True
		)

		df["answers"] = df["answers"].fillna("")
		df['domain'] = df['domain'].fillna('').apply(clean_text)
		
		logging.info("Tokenzing answers...")
		df.to_csv(output_path, index=False)
		print(f"Preprocessed data saved to {output_path}")

	except Exception as e:
		logging.error(f"An error occurred: {str(e)}")


def clean_text(text: str) -> str:
	if text == "":
		return ""

	text = re.sub(r"[^a-zA-Z0-9\sÀ-ÖØ-öø-ÿ]", "", text)
	text = re.sub(r'[^\w\s.,?!-]', '', text)
	text = re.sub(r"\s+", " ", text).strip()
	return text.lower()

		
