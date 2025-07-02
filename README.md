# docwise

**A Retrieval-Augmented Generation (RAG) system for document Q&A — built with Python, FAISS, and GPT.**

---

## Overview

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
| CLI Tool     | Python-based                  |
| Dev Features | dotenv, logging, modular code |

---

## Features

- Load `.txt`, `.md`, (coming soon `.pdf`, `.json`, `.docx`) documents
- Extract and clean usable text before embedding
- Chunk and embed with OpenAI embeddings
- Query with GPT-3.5 using top matching content
- Optional fallback if no match is found
- Includes `/reload` API and CLI tool for asking questions
- Fully backend-ready for integration or further development

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

### 3. Add your OpenAI API key

Create a `.env` file inside `/backend`:

```env
OPENAI_API_KEY=your-openai-key-here
```

### 4. Add Documents

Place your files into `backend/data/` — supported formats:
- `.txt`, `.md`, (coming soon`.pdf`, `.json`, `.docx`)

Each document will be cleaned and converted to plain text.

---

## How to Use

### Option A — Run API Server

```bash
uvicorn app.main:app --reload
```

Then visit:

- [http://localhost:8000/](http://localhost:8000) — health check
- [http://localhost:8000/reload](http://localhost:8000/reload) — re-index documents
- [http://localhost:8000/ask?question=your+question](http://localhost:8000/ask?question=your+question) — ask a question

---

### Option B — Run CLI

```bash
python cli.py
```

You'll enter an interactive session:

```text
📄 Welcome to docwise CLI — Ask your documents anything.
Type 'exit' to quit.

🧠 You: What is the PromptPilot Agent?
🤖 GPT: The PromptPilot Agent is...
```

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
│   ├── data/                # drop your docs here
│   ├── faiss_index/         # auto-generated vector DB
│   ├── cli.py               # CLI entry point
│   ├── .env
│   ├── requirements.txt
│   └── .gitignore
├── frontend/                # Coming soon
└── README.md
```

---

## Status

- [x] Project scaffolding
- [x] Document loading + cleaning
- [x] Embedding + FAISS index
- [x] GPT-powered answer generation
- [x] CLI interface
- [x] Reloadable `/reload` endpoint
- [ ] Frontend (Vite + Tailwind)

---

## Author

- Richard Hall

## Timeline

- Created: July 2, 2025

