import os
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path(__file__).parent.parent / "data"
FAISS_DIR = Path(__file__).parent.parent / "faiss_index"

def load_and_embed_documents():
    docs = []

    for file in DATA_DIR.glob("*.txt"):
        loader = TextLoader(str(file))
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embedding=embeddings)
    vectorstore.save_local(str(FAISS_DIR))

    return vectorstore

def ask_question(question: str) -> str:
    if not FAISS_DIR.exists():
        vectorstore = load_and_embed_documents()
    else:
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.load_local(str(FAISS_DIR), embeddings)

    retriever = vectorstore.as_retriever()
    docs = retriever.get_relevant_documents(question)
    context = "\n".join(doc.page_content for doc in docs)

    return f"Based on the documents:\n\n{context}\n\nAnswer: (This is where GPT would respond — coming next)"
