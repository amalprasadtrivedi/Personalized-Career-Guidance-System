from fastapi import FastAPI, HTTPException, Body, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from pathlib import Path
import pandas as pd
import joblib
import uvicorn
import os
import fitz  # PyMuPDF
import docx2txt
from starlette.responses import JSONResponse
from app.routes.career import router  # If using route-based modularization

# --------------------- FastAPI Initialization --------------------- #
app = FastAPI(title="Personalized Career Guidance System")

# Enable CORS (allow frontend to call backend APIs)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------- Load CSV Data --------------------- #
DATA_DIR = Path("app/data")
job_roles_df = pd.read_csv(DATA_DIR / "job_roles.csv")
skills_matrix_df = pd.read_csv(DATA_DIR / "skills_matrix.csv")
questions_df = pd.read_csv(DATA_DIR / "questions.csv")

# --------------------- Load ML Models --------------------- #
try:
    recommender_model = joblib.load("app/ml_models/recommender_model.pkl")
    vectorizer = joblib.load("app/ml_models/vectorizer.pkl")
except FileNotFoundError:
    recommender_model = None
    vectorizer = None
    print("⚠️ Recommender model or vectorizer not found.")

# --------------------- Pydantic Models --------------------- #
class ResumeInput(BaseModel):
    extracted_skills: List[str]

class TestAnswers(BaseModel):
    answers: List[str]

class ProfileInput(BaseModel):
    name: str
    cgpa: float
    interests: List[str]
    skills: List[str]
    preferred_category: Optional[str] = None

# --------------------- Resume Upload Endpoint --------------------- #
SKILL_KEYWORDS = [
    "python", "java", "c++", "machine learning", "data analysis", "deep learning",
    "django", "flask", "fastapi", "pandas", "numpy", "sql", "react", "html", "css"
]

RECOMMENDATION_MAP = {
    "machine learning": "Machine Learning Engineer",
    "data analysis": "Data Analyst",
    "deep learning": "AI Researcher",
    "django": "Backend Developer",
    "react": "Frontend Developer",
    "sql": "Database Engineer",
    "html": "Web Developer",
    "python": "Software Developer"
}

@app.post("/resume/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Uploads a resume in PDF or DOCX, extracts skills, and suggests career paths.
    """
    try:
        ext = os.path.splitext(file.filename)[1].lower()

        if ext not in [".pdf", ".docx"]:
            raise HTTPException(status_code=400, detail="Only PDF and DOCX formats are supported.")

        contents = await file.read()
        text = ""

        if ext == ".pdf":
            with open("temp_resume.pdf", "wb") as f:
                f.write(contents)
            with fitz.open("temp_resume.pdf") as doc:
                for page in doc:
                    text += page.get_text()
            os.remove("temp_resume.pdf")

        elif ext == ".docx":
            with open("temp_resume.docx", "wb") as f:
                f.write(contents)
            text = docx2txt.process("temp_resume.docx")
            os.remove("temp_resume.docx")

        text_lower = text.lower()
        extracted_skills = [skill for skill in SKILL_KEYWORDS if skill in text_lower]
        recommended_roles = list({RECOMMENDATION_MAP.get(skill) for skill in extracted_skills if skill in RECOMMENDATION_MAP})
        recommended_roles = [r for r in recommended_roles if r]

        return {
            "skills": extracted_skills,
            "recommendations": recommended_roles
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process resume: {str(e)}")

# --------------------- Resume Skill Matching Endpoint --------------------- #
@app.post("/analyze_resume/")
def analyze_resume(data: ResumeInput):
    """
    Matches extracted resume skills with careers from skills matrix.
    """
    matched_careers = []
    for _, row in skills_matrix_df.iterrows():
        career = row["career_name"]
        score = sum([row.get(skill, 0) for skill in data.extracted_skills])
        if score >= 3:
            matched_careers.append(career)
    return {"matched_careers": list(set(matched_careers))}

# --------------------- Psychometric Test: Get Questions --------------------- #
@app.get("/get_test_questions/")
def get_test_questions():
    """
    Returns 10 random psychometric test questions.
    """
    if len(questions_df) < 10:
        return {"error": "Not enough questions in dataset."}
    sample = questions_df.sample(10).to_dict(orient="records")
    return {"questions": sample}

# --------------------- Psychometric Test: Score & Recommend --------------------- #
@app.post("/score_test/")
def score_test(data: Dict[str, Any] = Body(...)):
    """
    Scores psychometric answers and recommends careers.
    """
    try:
        answers = data.get("answers", {})
        if not answers:
            return JSONResponse(status_code=400, content={"message": "No answers provided."})

        score = 0
        for a in answers.values():
            if a.lower() in ["agree", "strongly agree"]:
                score += 1
            elif a.lower() == "neutral":
                score += 0.5

        normalized_score = (score / len(answers)) * 100 if answers else 0

        if normalized_score >= 80:
            rec = ["AI/ML Engineer", "Data Scientist", "Research Analyst"]
        elif normalized_score >= 50:
            rec = ["Software Developer", "Business Analyst", "QA Engineer"]
        else:
            rec = ["Technical Support", "Sales Executive", "Customer Success"]

        return {"score": normalized_score, "recommendations": rec}

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error processing test: {str(e)}"})

# --------------------- Profile-based Career Recommendation --------------------- #
@app.post("/recommend_careers/")
def recommend_careers(profile: ProfileInput):
    """
    Recommends careers based on CGPA, interests, skills, and category.
    """
    roles = job_roles_df
    if profile.preferred_category:
        roles = roles[roles["category"] == profile.preferred_category]

    scored = []
    for _, row in roles.iterrows():
        required = row["required_skills"].split(", ")
        matched = len(set(profile.skills) & set(required))
        interest_match = len(set(profile.interests) & set(required))
        score = matched + 0.5 * interest_match + profile.cgpa
        scored.append((row["career_name"], score))

    top = sorted(scored, key=lambda x: x[1], reverse=True)[:5]
    return {"recommended_roles": [r[0] for r in top]}

# --------------------- Root Endpoint --------------------- #
@app.get("/")
def read_root():
    return {"message": "🎯 Career Guidance System API is running successfully!"}

# --------------------- Optional: Run with Python --------------------- #
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
