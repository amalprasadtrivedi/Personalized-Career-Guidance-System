import os
import shutil
from msilib.schema import File

import fitz
from fastapi import APIRouter, HTTPException, UploadFile
from pydantic import BaseModel
from typing import List
import pandas as pd
from pathlib import Path

from starlette.responses import JSONResponse

from app.main import app

# --------------------- Initialize Router --------------------- #
router = APIRouter()

# --------------------- Load Skills Matrix Data --------------------- #
DATA_DIR = Path("app/data")
skills_matrix_df = pd.read_csv(DATA_DIR / "skills_matrix.csv")

# --------------------- Request Model --------------------- #
class ResumeInput(BaseModel):
    extracted_skills: List[str]  # Skills parsed from resume

# --------------------- Resume Analyzer Endpoint --------------------- #
@router.post("/analyze")
def analyze_resume_skills(data: ResumeInput):
    if skills_matrix_df.empty:
        raise HTTPException(status_code=500, detail="Skills matrix data not available.")

    matched_careers = []

    # Iterate through each career and score based on matched skills
    for _, row in skills_matrix_df.iterrows():
        career = row["career_name"]
        score = sum([row.get(skill, 0) for skill in data.extracted_skills])
        if score >= 3:  # Threshold for recommendation
            matched_careers.append(career)

    return {"matched_careers": list(set(matched_careers))}

# --------------------- Resume Upload Endpoint --------------------- #
@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Uploads a resume file and saves it to the 'uploads' folder.
    """
    try:
        # Create uploads folder if it doesn't exist
        os.makedirs("uploads", exist_ok=True)

        # Save uploaded file
        file_location = os.path.join("uploads", file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return JSONResponse(content={
            "filename": file.filename,
            "message": "Resume uploaded successfully.",
            "path": file_location
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


# --------------------- Resume Upload & Parsing API --------------------- #
@app.post("/resume/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Uploads and parses a resume file (PDF), extracts text and basic keywords.
    This version uses PyMuPDF (fitz).
    """
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        contents = await file.read()

        # Save temporarily
        temp_path = "temp_resume.pdf"
        with open(temp_path, "wb") as f:
            f.write(contents)

        # Extract text using PyMuPDF
        doc = fitz.open(temp_path)
        text = ""
        for page in doc:
            text += page.get_text()

        doc.close()
        os.remove(temp_path)

        # Very basic keyword extraction — adjust as needed
        extracted_skills = []
        possible_skills = set(skills_matrix_df.columns[1:])  # Skip "career_name" column
        for skill in possible_skills:
            if skill.lower() in text.lower():
                extracted_skills.append(skill)

        return {"extracted_skills": extracted_skills, "raw_text": text[:500]}  # Limit raw_text to 500 chars
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
