from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
from pathlib import Path
import random

# --------------------- Initialize Router --------------------- #
router = APIRouter()

# --------------------- Load Questions --------------------- #
DATA_DIR = Path("app/data")
questions_df = pd.read_csv(DATA_DIR / "questions.csv")

# --------------------- Request Model --------------------- #
class TestAnswers(BaseModel):
    answers: List[str]  # List of selected options (e.g., A, B, C, D)

# --------------------- Provide Psychometric/Aptitude Questions --------------------- #
@router.get("/questions")
def get_test_questions():
    if questions_df.empty:
        raise HTTPException(status_code=500, detail="No test questions found.")

    sample_questions = questions_df.sample(10).to_dict(orient="records")
    return {"questions": sample_questions}

# --------------------- Evaluate Answers (Mock Logic) --------------------- #
@router.post("/evaluate")
def evaluate_test(answers: TestAnswers):
    if len(answers.answers) != 10:
        raise HTTPException(status_code=400, detail="Exactly 10 answers are required.")

    # Simple scoring logic: +1 for each correct option
    score = 0
    correct_answers = questions_df.sample(10)["correct_option"].tolist()
    for user_ans, correct_ans in zip(answers.answers, correct_answers):
        if user_ans.upper() == correct_ans.upper():
            score += 1

    result = "Strong Fit" if score >= 7 else "Moderate Fit" if score >= 4 else "Needs Development"

    return {
        "total_score": score,
        "evaluation": result,
        "message": f"You are a '{result}' for the targeted career paths."
    }
