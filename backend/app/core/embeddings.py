# app/core/embeddings.py
import os
from langchain.embeddings.base import Embeddings

# Check if OpenAI key exists
if os.getenv("OPENAI_API_KEY"):
    from langchain_openai import OpenAIEmbeddings

    def get_embeddings():
        return OpenAIEmbeddings(
            model="text-embedding-3-small",
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

else:
    # Dummy embeddings for testing
    import numpy as np

    class DummyEmbeddings(Embeddings):
        def embed_documents(self, texts):
            # Each text is mapped to a random vector of size 1536
            return [np.random.rand(1536).tolist() for _ in texts]

        def embed_query(self, text):
            return np.random.rand(1536).tolist()

    def get_embeddings():
        print("⚠️ Using Dummy Embeddings — no OpenAI key set")
        return DummyEmbeddings()
