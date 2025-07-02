from app.rag_engine import load_and_embed_documents, ask_question

# Always refresh vector store when CLI starts
load_and_embed_documents()  

def main():
    print("📄 Welcome to docwise CLI — Ask your documents anything.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("🧠 You: ")
        if query.lower() in ["exit", "quit"]:
            break

        answer = ask_question(query)
        print(f"\n🤖 GPT: {answer}\n")

if __name__ == "__main__":
    main()
