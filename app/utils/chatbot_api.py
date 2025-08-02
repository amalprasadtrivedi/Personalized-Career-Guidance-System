import requests
import os

# --------------------- Load GROKE API key --------------------- #
GROKE_API_KEY = os.getenv("GROKE_API_KEY", "your_groke_api_key_here")
GROKE_URL = "https://api.groke.ai/chat"

# --------------------- Interact with Groke Chatbot API --------------------- #
def query_chatbot(message: str, session_id: str = "default_user") -> dict:
    """
    Sends a message to the Groke Chatbot API and returns its response.

    Args:
        message (str): User input
        session_id (str): Session identifier to maintain context

    Returns:
        dict: API response or error
    """
    headers = {
        "Authorization": f"Bearer {GROKE_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "session_id": session_id,
        "query": message
    }

    try:
        response = requests.post(GROKE_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return {
            "response": data.get("response", "No response received."),
            "status": "success"
        }
    except requests.exceptions.RequestException as e:
        return {
            "response": f"API request failed: {str(e)}",
            "status": "error"
        }
