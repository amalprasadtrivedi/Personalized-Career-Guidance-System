# app/frontend/pages/5_💬_Chatbot.py

import streamlit as st
import requests

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="Career Chatbot", page_icon="💬", layout="wide")

# ----------------------------
# Sidebar Setup
# ----------------------------
with st.sidebar:
    st.header("📌 Navigation")
    st.markdown("**You are here:**")
    st.markdown("`💬 Career Guidance Chatbot`")
    st.markdown("""
        **Pages Available:**
        - 🧠 Psychometric Test  
        - 📊 Recommendation Dashboard  
        - 📚 Learning Resources  
        - 💬 Career Chatbot
    """)

    st.markdown("---")
    st.subheader("🔗 Connect with Me")

    # Portfolio Button
    st.markdown(
        """
        <a href="https://amalprasadtrivediportfolio.vercel.app/" target="_blank">
            <button style='width:100%; padding:10px; margin-bottom:10px; background-color:#4CAF50; color:white; border:none; border-radius:5px;'>
                🌐 My Portfolio
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    # LinkedIn Button
    st.markdown(
        """
        <a href="https://linkedin.com/posts/amalprasadtrivedi-aiml-engineer" target="_blank">
            <button style='width:100%; padding:10px; background-color:#0072b1; color:white; border:none; border-radius:5px;'>
                💼 LinkedIn Profile
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# Main Title and Description
# ----------------------------
st.title("💬 Career Guidance Chatbot")
st.subheader("Your Personalized Career Mentor")

st.markdown("""
Welcome to the interactive **AI-Powered Career Chatbot** 🤖  
You can ask anything about:
- Suitable careers based on your skills
- Learning paths and resources
- Required certifications or skillsets
- Colleges, job profiles, packages, etc.

Type your message below and get instant guidance tailored to your journey!
""")

# ----------------------------
# Session State for Chat History
# ----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------------
# Chat Input
# ----------------------------
API_URL = "http://localhost:8000/chatbot/respond"  # Ensure FastAPI is running

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("🗣️ Type your query:", key="user_input")
    submitted = st.form_submit_button("📤 Send")

    if submitted and user_input.strip():
        st.session_state.chat_history.append(("🧑‍💼 You", user_input))
        try:
            response = requests.post(API_URL, json={"message": user_input})
            if response.status_code == 200:
                bot_reply = response.json().get("reply", "🤖 Sorry, I didn’t get that.")
            else:
                bot_reply = "⚠️ Error: Chatbot backend not responding."
        except Exception as e:
            bot_reply = f"❌ Connection Error: {e}"

        st.session_state.chat_history.append(("🤖 Bot", bot_reply))

# ----------------------------
# Chat History Display
# ----------------------------
st.markdown("### 📝 Conversation History")

for sender, message in st.session_state.chat_history:
    if sender == "🧑‍💼 You":
        st.markdown(f"<div style='color:#1e88e5'><b>{sender}</b>: {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='color:#43a047'><b>{sender}</b>: {message}</div>", unsafe_allow_html=True)

# ----------------------------
# Clear Chat Button
# ----------------------------
st.markdown("---")
if st.button("🧹 Clear Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()
