import pandas as pd
import re

def clean_text(text):
	"""Cleans a given text by removing special characters, extra spaces, and making it lowercase.

	Args:
		text (string): Input text to clean
	"""
 
	if pd.isnull(text):
		return ""

	text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
	text = re.sub(r"\s+", " ", text).strip()
	return text.lower()


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
			"Résumé bref de la demande",
			"Commentaires", 
			"Lien avec le Memo", 
			"Action faite", 
			"Situation de handicap", 
			"Domaine de la question de droit"
		],
		inplace=True
	)
	
	df["Réponse écrite de DP"] = df["Réponse écrite de DP"].fillna("")
	df["Réponse écrite de DP"] = df["Réponse écrite de DP"].apply(clean_text)
	
	df.to_csv(output_path, index=False)
	print(f"Preprocessed data saved to {output_path}")