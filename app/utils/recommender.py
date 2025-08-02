import pandas as pd
import joblib
from typing import List

# Load the trained ML model and encoders
MODEL_PATH = "app/models/ml/career_model.pkl"
ENCODER_PATH = "app/models/ml/encoder.pkl"

# --------------------- Load the model and encoder once --------------------- #
try:
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
except Exception as e:
    model = None
    encoder = None
    print("Error loading model or encoder:", e)

# --------------------- Recommend career based on structured inputs --------------------- #
def recommend_career(stream: str, interest: str, skill: str, preferred_subject: str) -> dict:
    if not model or not encoder:
        return {"error": "Model or encoder not loaded."}

    # Prepare input for encoding
    input_df = pd.DataFrame([[stream, interest, skill, preferred_subject]],
                            columns=["Stream", "Interest", "Skill", "Subject"])

    # Encode categorical features
    try:
        input_encoded = encoder.transform(input_df)
        prediction = model.predict(input_encoded)[0]
        proba = model.predict_proba(input_encoded).max()
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}

    return {
        "recommended_career": prediction,
        "confidence": round(float(proba), 2)
    }

# --------------------- Recommend career based on extracted resume skills --------------------- #
def recommend_from_resume(skills: List[str]) -> dict:
    if not model or not encoder:
        return {"error": "Model or encoder not loaded."}

    # Combine top 3 skills for simplified input format
    skill_str = skills[:3] if len(skills) >= 3 else skills + ["none"] * (3 - len(skills))
    dummy_input = pd.DataFrame([["Any", "Unknown", skill_str[0], "General"]],
                               columns=["Stream", "Interest", "Skill", "Subject"])

    try:
        dummy_encoded = encoder.transform(dummy_input)
        prediction = model.predict(dummy_encoded)[0]
        proba = model.predict_proba(dummy_encoded).max()
    except Exception as e:
        return {"error": f"Resume prediction failed: {str(e)}"}

    return {
        "recommended_career": prediction,
        "confidence": round(float(proba), 2)
    }
