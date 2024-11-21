import os
import json
import pandas as pd
from dotenv import load_dotenv

from tqdm import tqdm

from src.pinecone.init import create_db
from src.pinecone.upsert import upsert_vectors

from langchain_community.embeddings import AzureOpenAIEmbeddings

load_dotenv()


def generate_embeddings(input_csv):
    df = pd.read_csv(input_csv)
    answers = df["answers"].tolist()
    questions = df["questions"].tolist()

    embeddings_function = AzureOpenAIEmbeddings(
        model='text-embedding-ada-002'
    )

    embeddings = []
    for idx, (question, answer) in enumerate(
        tqdm(
            zip(questions, answers),
            total=len(questions),
            desc="Embedding Progress"
        )
    ):
        answer_embedding = embeddings_function.embed_query(answer)
        embeddings.append((
            f"a_{idx}",
            answer_embedding,
            {
                "text": answer,
                "type": "answer",
                "question": question,
                "pair_id": idx
            }
        ))

        question_embedding = embeddings_function.embed_query(question)
        embeddings.append((
            f"q_{idx}",
            question_embedding,
            {
                "text": question,
                "type": "question",
                "answer": answer,
                "pair_id": idx
            }
        ))

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
