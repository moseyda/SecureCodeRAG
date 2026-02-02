from pydantic import BaseModel
from typing import List, Optional, Dict

class Vulnerability(BaseModel):
    type: str
    line: int
    snippet: str
    owasp: str

class Confidence(BaseModel):
    score: float
    level: str

class AnalysisResult(BaseModel):
    vulnerability: Vulnerability
    metadata: Optional[Dict[str, str]]
    confidence: Confidence
    explanation: str
    sources: List[Dict]

class AnalysisResponse(BaseModel):
    results: List[AnalysisResult]
