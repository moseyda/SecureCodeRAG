from app.core.llm import get_llm
from app.rag.prompts import EXPLANATION_PROMPT

class ExplanationGenerator:
    """Generates AI explanations for vulnerabilities using RAG context"""
    
    def __init__(self):
        self.llm = get_llm()
        self.prompt = EXPLANATION_PROMPT

    def generate_explanation(self, vulnerability: dict, context_docs: list) -> str:
        """
        Generate AI explanation for vulnerability using RAG context
        
        Args:
            vulnerability: Dict with 'type', 'line', 'code', 'severity'
            context_docs: Retrieved OWASP documentation chunks
            
        Returns:
            AI-generated explanation string
        """
        # Combine OWASP documentation context
        context = "\n\n".join([doc.page_content for doc in context_docs[:3]])
        
        if not context:
            context = "No additional context available."
        
        # Format prompt with vulnerability details
        prompt = self.prompt.format(
            vulnerability_type=vulnerability.get("type", "Unknown"),
            code_snippet=vulnerability.get("code", ""),
            context=context
        )
        
        try:
            # Generate explanation using Gemini
            response = self.llm.invoke(prompt)
            return response.content if hasattr(response, 'content') else str(response)
        except Exception as e:
            return f"Error generating explanation: {str(e)}"
