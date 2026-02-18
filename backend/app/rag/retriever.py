from app.vectorstore.index import get_vectorstore
from app.core.config import settings

class VulnerabilityRetriever:
    """Retrieves relevant OWASP documentation for detected vulnerabilities"""
    
    def __init__(self):
        self.vectorstore = get_vectorstore()
        self.top_k = settings.TOP_K
    
    def retrieve(self, vulnerability_type: str, top_k: int = None):
        """
        Retrieve relevant documentation for a vulnerability type
        
        Args:
            vulnerability_type: Type of vulnerability (e.g., "SQL Injection")
            top_k: Number of documents to retrieve (default: from settings)
            
        Returns:
            List of relevant document chunks
        """
        if top_k is None:
            top_k = self.top_k
        
        # Search vectorstore for relevant OWASP docs
        try:
            docs = self.vectorstore.similarity_search(
                query=vulnerability_type,
                k=top_k
            )
            return docs
        except Exception as e:
            print(f"Error retrieving documents: {e}")
            return []
