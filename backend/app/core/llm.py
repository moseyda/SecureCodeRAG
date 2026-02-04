import os
from app.core.config import settings

# Try to import ChatOpenAI if available
try:
    from langchain_openai import ChatOpenAI
except ImportError:
    ChatOpenAI = None

# Dummy LLM for testing
class DummyLLM:
    def __call__(self, prompt, **kwargs):
        return f"Dummy explanation for: {prompt}"
    
    def predict(self, text, **kwargs):
        """LangChain compatibility method"""
        return f"Dummy explanation: This code may have security issues. Context: {text[:100]}..."
    
    def invoke(self, messages, **kwargs):
        """LangChain LCEL compatibility"""
        text = str(messages)  # use this everywhere
        return type(
            'Response',
            (),
            {'content': f"Dummy explanation for the security issue found in the code. Context: {text[:100]}..."}
        )()

def get_llm():
    # If OPENAI_API_KEY exists and ChatOpenAI is available, use real LLM
    if os.getenv("OPENAI_API_KEY") and ChatOpenAI is not None:
        return ChatOpenAI(
            model=settings.LLM_MODEL,
            temperature=0
        )
    # Otherwise, use dummy LLM for local testing
    print("⚠️ Using Dummy LLM — no OpenAI key set")
    return DummyLLM()