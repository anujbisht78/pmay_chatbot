import pandas as pd
from sentence_transformers import SentenceTransformer


# LOAD DATASET
FILE_PATH = "PMAY New QAs.xlsx"

df = pd.read_excel(FILE_PATH)

df = df[
    ['Question', 'Answer']
].dropna()

questions = (
    df['Question']
    .astype(str)
    .str.lower()
    .tolist()
)

answers = (
    df['Answer']
    .astype(str)
    .tolist()
)


# LOAD MODEL

print("Loading embedding model...")

model = SentenceTransformer(
    'multi-qa-MiniLM-L6-cos-v1'
)

print("Creating embeddings...")

question_embeddings = model.encode(
    questions,
    convert_to_numpy=True,
    show_progress_bar=True
)

print("Embeddings ready!")