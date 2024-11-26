import docx
from src.data_preprocessing.preprocess import clean_text
from src.data_preprocessing.embeddings import upload_embeddings
from langchain_openai import AzureOpenAIEmbeddings
from tqdm import tqdm
import json

docx_filepath = 'data/questions.docx'


def get_questions(filename):
	doc = docx.Document(filename)
	sections = {}

	current_header = None
	current_content = []
	arrived = False

	for paragraph in doc.paragraphs:
		if paragraph.text == 'Éléments de réponse récurrents :':
			arrived = True

		if paragraph.style.name.startswith('Heading') and arrived:
			if current_header is not None:
				sections[current_header] = '\n'.join(current_content)

			current_header = paragraph.text
			current_content = []
		else:
			current_content.append(paragraph.text)

	if current_header is not None:
		sections[current_header] = '\n'.join(current_content)

	return sections


def chunk_text(text, chunk_size=250, overlap=50):
	chunks = []
	start = 0
	while start < len(text):
		end = min(start + chunk_size, len(text))
		chunks.append(text[start:end])
		start += chunk_size - overlap
	return chunks


def chunk_doc():
	text = get_questions(docx_filepath)
	answers = list(text.values())
 
	embeddings = []
	embeddings_function = AzureOpenAIEmbeddings(
		model='text-embedding-ada-002'
	)

	for idx, (answers) in enumerate(
			tqdm(
				answers,
				total=len(answers),
				desc="Embedding Progress"
			)
	):
		chunked_answer = chunk_text(answers)
		for i in range(len(chunked_answer)):
			cleaned = clean_text(chunked_answer[i])
			embed = embeddings_function.embed_query(cleaned)

			embeddings.append((
				f"doc_{idx}_chunk_{i}",
				embed,
				{
					"text": list(text.keys())[idx],
					"tokens": answers,
					"type": "answer",
				}
			))
   
	with open('doc-embeds.json', 'w') as f:
		json.dump(embeddings, f)

	return embeddings