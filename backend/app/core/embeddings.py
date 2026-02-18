import os
import numpy as np
from langchain.embeddings.base import Embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from app.core.config import settings

# Optional Gemini import
if os.getenv("GEMINI_API_KEY"):
    from langchain_google_genai import GoogleGenerativeAIEmbeddings


class DummyEmbeddings(Embeddings):
    def embed_documents(self, texts):
        # Each text is mapped to a random vector of size 768
        return [np.random.rand(768).tolist() for _ in texts]

    def embed_query(self, text):
        return np.random.rand(768).tolist()


def get_embeddings():
    """
    Returns Google Generative AI embeddings if API key is set.
    Falls back to HuggingFace embeddings (free, offline).
    Falls back to DummyEmbeddings if needed.
    """
    if os.getenv("GEMINI_API_KEY"):
        try:
            # Use the correct Gemini embedding model
            return GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
        except Exception as e:
            print(f"⚠️ Gemini embeddings failed: {e}")
            print("⚠️ Falling back to HuggingFace embeddings...")
    
    try:
        return HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    except Exception:
        print("⚠️ Using Dummy Embeddings — fallback mode")
        return DummyEmbeddings()
