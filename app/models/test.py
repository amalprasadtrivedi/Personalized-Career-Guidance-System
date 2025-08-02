from pydantic import BaseModel
from typing import List

# --------------------- Model for a test question --------------------- #
class TestQuestion(BaseModel):
    id: int
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_option: str  # Used internally, not exposed to users

# --------------------- Model to send multiple questions --------------------- #
class TestQuestionList(BaseModel):
    questions: List[TestQuestion]

# --------------------- Model for user's submitted answers --------------------- #
class TestAnswers(BaseModel):
    answers: List[str]  # User-selected options, length must match number of questions

# --------------------- Evaluation result schema --------------------- #
class EvaluationResult(BaseModel):
    total_score: int
    evaluation: str
    message: str