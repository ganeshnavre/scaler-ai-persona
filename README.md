# Ganesh AI Representative

AI-powered personal representative chatbot built using Retrieval-Augmented Generation (RAG). The chatbot answers questions about Ganesh Navre's skills, projects, education, and experience using resume and project data.

## Project Overview

This project creates an AI persona of Ganesh Navre that can:

- Answer questions about skills and experience
- Explain projects in detail
- Provide information from resume and project documents
- Use RAG to ensure grounded responses
- Generate responses using OpenRouter LLM

## Architecture

Resume PDF + Projects Data
        |
        v
    Ingestion
        |
        v
 Sentence Transformers
    Embeddings
        |
        v
     ChromaDB
   Vector Store
        |
        v
 User Question
        |
        v
 Similarity Search
        |
        v
 Retrieved Context
        |
        v
 OpenRouter LLM
        |
        v
 Final Response

## Tech Stack

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- OpenRouter
- HuggingFace
- PyPDF
- RAG Architecture

## Features

- Resume-based question answering
- Project-based retrieval
- Vector search using ChromaDB
- Grounded responses
- Streamlit chat interface
- OpenRouter LLM integration

## Project Structure

```text
scaler-ai-persona/
│
├── app.py
├── rag.py
├── ingest.py
├── requirements.txt
│
├── resume/
│   └── Ganesh Navre AI Engineer.pdf
│
├── data/
│   └── projects.txt
│
└── chroma_db/
```

## Local Setup

### Clone Repository

```bash
git clone https://github.com/ganeshnavre/scaler-ai-persona.git
cd scaler-ai-persona
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Environment Variable

Create `.env`

```env
OPENROUTER_API_KEY=your_api_key
```

### Build Vector Database

```bash
python ingest.py
```

### Run Application

```bash
streamlit run app.py
```

## Deployment

Chat URL:



Example:

https://your-app.streamlit.app

## Cost Breakdown

### Development Cost

- ChromaDB: Free
- Sentence Transformers: Free
- Streamlit Cloud: Free
- GitHub: Free

### Inference Cost

- OpenRouter Free Model:
  - Cost: $0
  - Model: openai/gpt-oss-120b:free

Approximate chat session cost:
- Development stage: Free

## Future Improvements

- Voice Agent Integration
- Calendar Booking
- Multi-turn Memory
- GitHub Repository Ingestion
- Evaluation Dashboard

## Author

Ganesh Navre

AI Engineer | Data Analyst | Machine Learning Enthusiast
