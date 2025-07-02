from fastapi import FastAPI
from app.rag_engine import ask_question, load_and_embed_documents

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to docwise!"}

@app.get("/ask")
def ask(question: str):
    answer = ask_question(question)
    return {"question": question, "answer": answer}

@app.get("/reload")
def reload_docs():
    load_and_embed_documents()
    return {"message": "Document vector store reloaded."}
