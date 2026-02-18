from pydantic import BaseModel, Field

class CodeRequest(BaseModel):
    code: str = Field(..., description="Source code to analyze for vulnerabilities")
    language: str = Field(default="python", description="Programming language")
    
    class Config:
        json_schema_extra = {
            "example": {
                "code": "query = f\"SELECT * FROM users WHERE id={user_id}\"",
                "language": "python"
            }
        }
