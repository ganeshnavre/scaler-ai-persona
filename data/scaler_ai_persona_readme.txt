Ganesh AI Representative

AI-powered personal representative chatbot built using Retrieval-Augmented Generation (RAG).

Project Overview

This project creates an AI persona of Ganesh Navre that can:

- Answer questions about skills and experience
- Explain projects in detail
- Provide information from resume and project documents
- Use RAG to ensure grounded responses
- Generate responses using OpenRouter LLM

Architecture

Resume PDF + Projects Data
→ Ingestion
→ Sentence Transformers Embeddings
→ ChromaDB Vector Store
→ Similarity Search
→ Retrieved Context
→ OpenRouter LLM
→ Final Response

Tech Stack

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- OpenRouter
- HuggingFace
- PyPDF
- RAG Architecture

Features

- Resume-based question answering
- Project-based retrieval
- Vector search using ChromaDB
- Grounded responses
- Streamlit chat interface
- OpenRouter LLM integration

Project Structure

- app.py
- rag.py
- ingest.py
- requirements.txt
- resume/Ganesh Navre AI Engineer.pdf
- data/projects.txt

Deployment

Chat URL:
https://ganeshnavre-scaler-ai-persona-app-22wqaw.streamlit.app/

GitHub Repository:
https://github.com/ganeshnavre/scaler-ai-persona

Cost Breakdown

Development Cost:
- ChromaDB: Free
- Sentence Transformers: Free
- Streamlit Cloud: Free
- GitHub: Free

Inference Cost:
- OpenRouter Free Model
- Model: openai/gpt-oss-120b:free

Future Improvements

- Voice Agent Integration
- Calendar Booking
- Multi-turn Memory
- GitHub Repository Ingestion
- Evaluation Dashboard

Author

Ganesh Navre
AI Engineer | Data Analyst | Machine Learning Enthusiast