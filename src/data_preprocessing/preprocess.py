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
	if text == "":
		return ""

	text = re.sub(r"[^a-zA-Z0-9\sÀ-ÖØ-öø-ÿ]", "", text)
	text = re.sub(r'[^\w\s.,?!-]', '', text)
	text = re.sub(r"\s+", " ", text).strip()
	return text.lower()

def tokenize_text(text: str) -> List[str]:
	# text = unicodedata.normalize('NFKD', text)
	
	# text = ''.join([c for c in text if not unicodedata.combining(c)])
	
	text = text.lower()
	
	text = re.sub(r'[^\w\s.,?!-]', '', text)
	
	tokens = nltk.word_tokenize(text)
	
	stop_words = set(stopwords.words('french'))
	tokens = [token for token in tokens if token not in stop_words]
	
	lemmatizer = WordNetLemmatizer()
	tokens = [lemmatizer.lemmatize(token) for token in tokens]
	
	tokens = [token for token in tokens if len(token) > 1]
	
	return tokens


def preprocess_csv(file_path, output_path):
    """
    Reads, cleans, and preprocesses the text in a CSV file.
    Args:
                                                                                                                                                                                                                                                                    file_path (str): Path to the input CSV file.
                                                                                                                                                                                                                                                                    output_path (str): Path to save the cleaned CSV file.
    """

    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip()

    df.set_index("Numéro de dossier", inplace=True)

    df.drop(
        columns=[
            "Commentaires",
            "Lien avec le Memo",
            "Action faite",
            "Situation de handicap",
            "Domaine de la question de droit"
        ],
        inplace=True
    )

    df.rename(
        columns={
            "Résumé bref de la demande": "questions",
            "Réponse écrite de DP": "answers"
        },
        inplace=True
    )

    df["answers"] = df["answers"].fillna("")
    df["answers"] = df["answers"].apply(
        clean_text
    )

    df["questions"] = df["questions"].fillna("")
    df["questions"] = df["questions"].apply(
        clean_text
    )

    df.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")
