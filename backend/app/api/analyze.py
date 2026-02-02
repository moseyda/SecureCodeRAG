from fastapi import APIRouter, HTTPException
import traceback

from app.security.static_scan import detect_vulnerabilities
from app.security.confidence import calculate_confidence
from app.security.vulnerability_map import get_metadata

from app.rag.retriever import retrieve_docs
from app.rag.generator import generate_explanation

from app.schemas.request import CodeAnalysisRequest
from app.schemas.response import AnalysisResponse

router = APIRouter()

@router.post(
    "/analyze",
    response_model=AnalysisResponse,
    summary="Analyze source code for security vulnerabilities"
)
def analyze_code(payload: CodeAnalysisRequest):
    """
    Hybrid static-analysis + RAG-based secure code review.
    """
    try:
        code = payload.code
        print(f"📝 Analyzing code:\n{code}")  # Show full code
        
        vulns = detect_vulnerabilities(code)
        print(f"🔍 Found {len(vulns)} vulnerabilities")
        print(f"🔍 Vulnerabilities: {vulns}")  # Show what was found
        
        results = []

        # Explicit handling: no vulnerabilities found
        if not vulns:
            print("⚠️ No vulnerabilities detected by static scanner")
            return {"results": []}

        for v in vulns:
            print(f"Processing vulnerability: {v['type']}")  # Debug log
            docs = retrieve_docs(v["type"])

            # Defensive: do not hallucinate explanations
            if not docs:
                explanation = (
                    "Insufficient supporting evidence was found in the "
                    "security knowledge base to confidently explain this issue."
                )
            else:
                explanation = generate_explanation(v, docs)

            metadata = get_metadata(v["type"])

            confidence = calculate_confidence(
                static_hits=1,
                retrieved_docs=len(docs)
            )

            results.append({
                "vulnerability": v,
                "metadata": metadata,
                "confidence": confidence,
                "explanation": explanation,
                "sources": [doc.metadata for doc in docs]
            })

        return {"results": results}
    
    except Exception as e:
        print(f"❌ Error in analyze_code: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))