from pydantic import BaseModel, Field


class ResumeReview(BaseModel):
    score: int = Field(ge=0, le=100)
    ats_score: int = Field(ge=0, le=100)
    summary: str
    strengths: list[str]
    weaknesses: list[str]
    suggestions: list[str]