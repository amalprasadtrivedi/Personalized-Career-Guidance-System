from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd
import joblib
from pathlib import Path

# --------------------- Initialize Router --------------------- #
router = APIRouter()

# --------------------- Load Data --------------------- #
DATA_DIR = Path("app/data")
job_roles_df = pd.read_csv(DATA_DIR / "job_roles.csv")

# --------------------- Load Model --------------------- #
try:
    recommender_model = joblib.load("app/ml_models/recommender_model.pkl")
    vectorizer = joblib.load("app/ml_models/vectorizer.pkl")
except:
    recommender_model = None
    vectorizer = None

# --------------------- Request Model --------------------- #
class ProfileInput(BaseModel):
    name: str
    cgpa: float
    interests: List[str]
    skills: List[str]
    preferred_category: Optional[str] = None

# --------------------- Recommend Careers --------------------- #
@router.post("/recommend")
def recommend_careers(profile: ProfileInput):
    if job_roles_df.empty:
        raise HTTPException(status_code=500, detail="Job role data not found.")

    # Step 1: Filter based on category
    filtered_df = job_roles_df
    if profile.preferred_category:
        filtered_df = filtered_df[job_roles_df["category"] == profile.preferred_category]

    # Step 2: Score careers based on skills + interests + CGPA
    match_scores = []
    for _, row in filtered_df.iterrows():
        required_skills = row["required_skills"].split(", ")
        matched_skills = len(set(profile.skills) & set(required_skills))
        matched_interests = len(set(profile.interests) & set(required_skills))
        score = matched_skills + 0.5 * matched_interests + profile.cgpa
        match_scores.append((row["career_name"], score))

    # Step 3: Return Top 5 recommendations
    sorted_roles = sorted(match_scores, key=lambda x: x[1], reverse=True)
    top_roles = [role for role, score in sorted_roles[:5]]

    return {"recommended_careers": top_roles}
