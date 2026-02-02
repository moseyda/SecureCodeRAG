import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "Secure Code Review RAG Agent"

    # API keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Models
    LLM_MODEL = "gpt-4o-mini"
    EMBEDDING_MODEL = "text-embedding-3-small"

    # Vector store
    VECTORSTORE_PATH = "vectorstore"
    TOP_K = 4

    # Confidence thresholds
    CONFIDENCE_HIGH = 0.75
    CONFIDENCE_MEDIUM = 0.45

settings = Settings()
