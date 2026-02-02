import os
from langchain_community.vectorstores import FAISS
from app.core.embeddings import get_embeddings
from app.core.config import settings

def load_vectorstore():
    """
    Load existing FAISS index from disk.
    Fail fast if it does not exist.
    """
    if not os.path.exists(settings.VECTORSTORE_PATH):
        raise FileNotFoundError(
            "Vectorstore not found. Run ingest.py first."
        )

    embeddings = get_embeddings()

    return FAISS.load_local(
        settings.VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
