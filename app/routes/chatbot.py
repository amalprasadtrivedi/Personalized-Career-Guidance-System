from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import httpx
import os
from dotenv import load_dotenv

# --------------------- Load Environment Variables --------------------- #
load_dotenv()
GROKE_API_KEY = os.getenv("GROKE_API_KEY")
GROKE_API_URL = "https://api.groke.ai/v1/chat"

# --------------------- Initialize Router --------------------- #
router = APIRouter()

# --------------------- Request and Response Models --------------------- #
class ChatRequest(BaseModel):
    user_id: str
    message: str
    context: Optional[str] = "You are a career counselor chatbot."

# --------------------- Chat Endpoint --------------------- #
@router.post("/ask")
def ask_chatbot(query: ChatRequest):
    if not GROKE_API_KEY:
        raise HTTPException(status_code=500, detail="Groke API key not set.")

    headers = {
        "Authorization": f"Bearer {GROKE_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "user_id": query.user_id,
        "message": query.message,
        "context": query.context
    }

    try:
        response = httpx.post(GROKE_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        reply = response.json().get("reply", "I'm sorry, I didn't understand that.")
        return {"reply": reply}

    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"Groke API error: {str(e)}")
