from app.core.config import settings

def calculate_confidence(vulnerability: dict, context_docs: list) -> float:
    """
    Calculate confidence score for vulnerability detection
    
    Args:
        vulnerability: Detected vulnerability details
        context_docs: Retrieved OWASP documentation
        
    Returns:
        Confidence score between 0 and 1
    """
    score = 0.5  # Base score
    
    # High severity increases confidence
    if vulnerability.get('severity') == 'critical':
        score += 0.3
    elif vulnerability.get('severity') == 'high':
        score += 0.2
    
    # Having relevant documentation increases confidence
    if context_docs and len(context_docs) > 0:
        score += 0.2
    
    # Cap at 1.0
    return min(score, 1.0)
