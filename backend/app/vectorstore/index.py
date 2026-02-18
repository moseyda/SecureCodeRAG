import os
from langchain_community.vectorstores import FAISS
from app.core.embeddings import get_embeddings
from app.core.config import settings

def get_vectorstore():
    """
    Load the FAISS vectorstore from disk
    
    Returns:
        FAISS vectorstore instance
    """
    vectorstore_path = settings.VECTORSTORE_PATH
    
    if not os.path.exists(vectorstore_path):
        raise FileNotFoundError(
            f"Vectorstore not found at {vectorstore_path}. "
            f"Run 'python -m app.vectorstore.ingest' first."
        )
    
    embeddings = get_embeddings()
    vectorstore = FAISS.load_local(
        vectorstore_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    return vectorstore
