import os
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_db")

collections = [c.name for c in client.list_collections()]

if "ganesh_resume" not in collections:
    import ingest

collection = client.get_collection("ganesh_resume")

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_context(query):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    docs = results["documents"][0]

    return "\n".join(docs)