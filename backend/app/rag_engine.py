import os
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path(__file__).parent.parent / "data"
FAISS_DIR = Path(__file__).parent.parent / "faiss_index"

def load_and_embed_documents():
    docs = []

    for file in DATA_DIR.glob("*.txt"):
        loader = TextLoader(str(file), encoding="utf-8", autodetect_encoding=True)

        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embedding=embeddings)
    vectorstore.save_local(str(FAISS_DIR))

    return vectorstore

def ask_question(question: str) -> str:
    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    if not FAISS_DIR.exists():
        vectorstore = load_and_embed_documents()
    else:
        vectorstore = FAISS.load_local(str(FAISS_DIR), embeddings)

    retriever = vectorstore.as_retriever()

    prompt_template = """
    Use the following context to answer the user's question.
    If the answer cannot be found in the context, say "I couldn't find the answer in the provided documents."

    Context:
    {context}

    Question:
    {question}
    """

    prompt = PromptTemplate.from_template(prompt_template)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=False,
    )

    result = qa_chain.run(question)
    return result
