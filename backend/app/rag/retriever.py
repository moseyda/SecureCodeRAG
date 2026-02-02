from app.vectorstore.index import load_vectorstore
from app.core.config import settings

vectorstore = load_vectorstore()

def retrieve_docs(query: str):
    """
    Retrieve relevant security documentation for a vulnerability type.
    """
    return vectorstore.similarity_search(
        query,
        k=settings.TOP_K
    )
