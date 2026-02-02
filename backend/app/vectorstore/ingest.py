import os
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


from app.core.embeddings import get_embeddings
from app.core.config import settings

DATA_DIR = "data/owasp_docs"

def ingest_documents():
    documents = []

    for file in os.listdir(DATA_DIR):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(DATA_DIR, file))
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local(settings.VECTORSTORE_PATH)

    print(f"Ingested {len(chunks)} chunks into vectorstore.")

if __name__ == "__main__":
    ingest_documents()
