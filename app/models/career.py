from pydantic import BaseModel
from typing import Optional

# --------------------- Input schema for career prediction --------------------- #
class CareerInput(BaseModel):
    stream: str
    interest: str
    skill: str
    preferred_subject: str

# --------------------- Output schema for predicted career --------------------- #
class CareerPrediction(BaseModel):
    recommended_career: str
    confidence: float  # Confidence score or probability (0 to 1)
    description: Optional[str] = None  # Optional description or details

# --------------------- Resume to career mapping schema --------------------- #
class ResumeCareerPrediction(BaseModel):
    extracted_skills: list[str]
    recommended_career: str
    confidence: float
