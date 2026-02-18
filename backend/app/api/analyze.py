from fastapi import APIRouter
from app.schemas.request import CodeRequest
from app.schemas.response import AnalysisResponse
from app.security.static_scan import StaticScanner
from app.rag.retriever import VulnerabilityRetriever
from app.rag.generator import ExplanationGenerator
from app.security.confidence import calculate_confidence

router = APIRouter()
scanner = StaticScanner()
retriever = VulnerabilityRetriever()
generator = ExplanationGenerator()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_code(request: CodeRequest):
    """Analyze code for vulnerabilities with AI explanations"""
    
    # Step 1: Static scan for vulnerabilities
    vulnerabilities = scanner.scan(request.code)
    
    results = []
    for vuln in vulnerabilities:
        # Step 2: Retrieve relevant OWASP docs using RAG
        context_docs = retriever.retrieve(vuln["type"])
        
        # Step 3: Generate AI explanation with context
        explanation = generator.generate_explanation(vuln, context_docs)
        
        # Step 4: Calculate confidence score
        confidence = calculate_confidence(vuln, context_docs)
        
        results.append({
            "type": vuln["type"],
            "severity": vuln["severity"],
            "line": vuln["line"],
            "code": vuln["code"],
            "explanation": explanation,
            "confidence": confidence
        })
    
    return AnalysisResponse(
        vulnerabilities=results,
        total_vulnerabilities=len(results)
    )
