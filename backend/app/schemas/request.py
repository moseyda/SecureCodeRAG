from pydantic import BaseModel, Field

class CodeAnalysisRequest(BaseModel):
    code: str = Field(
        ...,
        description="Source code to be analyzed for security vulnerabilities"
    )
