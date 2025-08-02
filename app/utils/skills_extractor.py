import re
from typing import List
import spacy

# Load spaCy's English language model for NLP processing
nlp = spacy.load("en_core_web_sm")

# Predefined list of technical and soft skills (can be extended)
KNOWN_SKILLS = [
    "python", "java", "c++", "machine learning", "data analysis",
    "deep learning", "nlp", "react", "node.js", "sql",
    "communication", "leadership", "teamwork", "problem-solving",
    "tensorflow", "pytorch", "xgboost", "fastapi", "streamlit"
]


# --------------------- Clean and normalize text --------------------- #
def clean_text(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove punctuation
    return text.lower()


# --------------------- Extract relevant skills using spaCy and keyword match --------------------- #
def extract_skills_from_text(text: str) -> List[str]:
    cleaned = clean_text(text)
    doc = nlp(cleaned)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]

    extracted = []
    for skill in KNOWN_SKILLS:
        skill_tokens = skill.split()
        if all(word in tokens for word in skill_tokens):
            extracted.append(skill)
    return list(set(extracted))  # Remove duplicates


# --------------------- Extract skills from a resume string --------------------- #
def extract_resume_skills(resume_text: str) -> List[str]:
    return extract_skills_from_text(resume_text)


# Example (can be removed in production)
if __name__ == "__main__":
    sample_resume = """
        I am a passionate data science enthusiast with experience in Python,
        machine learning, deep learning, and NLP. I have worked on projects
        using TensorFlow, scikit-learn, and FastAPI.
    """
    skills = extract_resume_skills(sample_resume)
    print("Extracted Skills:", skills)
