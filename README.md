# docwise

**A Retrieval-Augmented Generation (RAG) system for document Q&A — built with Python, FAISS, and GPT.**

---

## Overview

`docwise` is a full-stack AI application that lets users upload `.txt` or `.md` documents, index them into a vector store using OpenAI embeddings, and query them using GPT-based natural language prompts. It's built with modern Python practices and will evolve into a production-grade developer portfolio project.

---

## Tech Stack

| Layer        | Tech                          |
|--------------|-------------------------------|
| Language     | Python 3.10+                  |
| Backend      | FastAPI                       |
| LLM          | OpenAI GPT (via API)          |
| Embeddings   | OpenAI `text-embedding-ada-002` |
| Vector DB    | FAISS (local)                 |
| Frontend     | (Coming soon) Vite + Tailwind |
| Dev Features | dotenv, logging, modular code |

---

## Features

- Upload `.txt` or `.md` documents
- Split, embed, and store content in FAISS
- Ask natural language questions over your docs
- GPT-powered answers grounded in document context
- Modular and testable FastAPI backend
- (Planned) Modern frontend with Vite + Tailwind CSS

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/docwise.git
cd docwise/backend
```

### 2. Set up your environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file inside `/backend`:

```env
OPENAI_API_KEY=your-openai-key-here
```

### 4. Run the App

```bash
uvicorn app.main:app --reload
```

Then visit: [http://localhost:8000](http://localhost:8000)

---

## Folder Structure

```
docwise/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── rag_engine.py
│   │   ├── config.py
│   │   └── utils.py
│   ├── data/
│   ├── faiss_index/
│   ├── .env
│   ├── requirements.txt
│   └── .gitignore
├── frontend/              # Coming soon
└── README.md
```

---

## Status

- [x] Project scaffolding
- [x] Document loading and chunking
- [x] Embedding + FAISS index
- [x] Question-answering route (FastAPI)
- [ ] GPT-powered answer generation
- [ ] Minimal CLI / test interface
- [ ] Frontend (Vite + Tailwind)

---

## Author

- Richard Hall

## Timeline

- Created: July 2, 2025
