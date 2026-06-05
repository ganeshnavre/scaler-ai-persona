import os
import chromadb
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader

# Chroma DB
client = chromadb.PersistentClient(path="chroma_db")

try:
    client.delete_collection("ganesh_resume")
except:
    pass

collection = client.create_collection("ganesh_resume")

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# =========================
# RESUME LOAD
# =========================

pdf_path = "resume/Ganesh Navre AI Engineer.pdf"

reader = PdfReader(pdf_path)

resume_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text + "\n"

# =========================
# PROJECTS LOAD
# =========================

projects_path = "data/projects.txt"

projects_text = ""

if os.path.exists(projects_path):
    with open(projects_path, "r", encoding="utf-8") as f:
        projects_text = f.read()

# =========================
# COMBINE DATA
# =========================

full_text = resume_text + "\n\n" + projects_text

# Chunking
chunk_size = 800

chunks = []

for i in range(0, len(full_text), chunk_size):
    chunks.append(full_text[i:i + chunk_size])

# Embeddings
embeddings = model.encode(chunks).tolist()

# Store in ChromaDB
collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

print("Resume + Projects loaded successfully!")
print(f"Total chunks: {len(chunks)}")