import os
from app.core.config import settings

# Try to import Gemini if available
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    ChatGoogleGenerativeAI = None

# Dummy LLM for testing
class DummyLLM:
    def __call__(self, prompt, **kwargs):
        return f"Dummy explanation for: {prompt}"
    
    def predict(self, text, **kwargs):
        """LangChain compatibility method"""
        return f"Dummy explanation: This code may have security issues. Context: {text[:100]}..."
    
    def invoke(self, messages, **kwargs):
        """LangChain LCEL compatibility"""
        text = str(messages)
        return type(
            'Response',
            (),
            {'content': f"Dummy explanation for the security issue found in the code. Context: {text[:100]}..."}
        )()

def get_llm():
    # If GEMINI_API_KEY exists and ChatGoogleGenerativeAI is available, use Gemini
    if os.getenv("GEMINI_API_KEY") and ChatGoogleGenerativeAI is not None:
        return ChatGoogleGenerativeAI(
            model=settings.LLM_MODEL,
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0,
            convert_system_message_to_human=True
        )
    # Otherwise, use dummy LLM for local testing
    print("[WARNING] Using Dummy LLM - no Gemini API key set")
    return DummyLLM()