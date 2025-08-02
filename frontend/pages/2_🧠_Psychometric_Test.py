import streamlit as st
import requests

# ----------------------------
# Streamlit Page Config
# ----------------------------
st.set_page_config(page_title="Psychometric Career Test", page_icon="🧠")

# ----------------------------
# Sidebar Layout
# ----------------------------
with st.sidebar:
    st.markdown("## 🧭 Navigation")
    st.info("**Current Page:** Psychometric Test\n\nExplore how your personality matches various career paths.")
    st.markdown("---")

    st.markdown("### 📄 Pages Available:")
    st.markdown("""
    - 📄 Resume Parser  
    - 🧠 Psychometric Test  
    - 📊 Analytics Dashboard  
    - 💬 Chat-based Guidance  
    """)

    st.divider()

    # External Links
    st.markdown("### 🔗 Connect with Developer")
    st.link_button("🌐 Portfolio", "https://amalprasadtrivediportfolio.vercel.app/")
    st.link_button("🔗 LinkedIn", "https://linkedin.com/posts/amalprasadtrivedi-aiml-engineer")

    # Footer badge
    st.markdown(
        """
        <style>
        .sidebar-button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            margin-top: 10px;
        }
        .sidebar-button img {
            width: 100%;
            max-width: 250px;
        }
        </style>
        <div class="sidebar-button-container">
            <a href="https://amalprasadtrivediportfolio.vercel.app/" target="_blank" class="sidebar-button">
                <img src="https://img.shields.io/badge/Created%20by-Amal%20Prasad%20Trivedi-blue">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# Title & Description
# ----------------------------
st.title("🧠 Psychometric Career Test")
st.markdown("""
This AI-powered test evaluates your cognitive patterns, personality traits, and interests to recommend the best-suited career domains.

Please answer each question honestly. The more accurate your responses, the better the recommendations.
""")

# ----------------------------
# API Endpoints
# ----------------------------
QUESTION_API_URL = "http://localhost:8000/get_test_questions/"
SCORE_API_URL = "http://localhost:8000/score_test/"

# ----------------------------
# Fetch Questions from Backend
# ----------------------------
@st.cache_data
def fetch_questions():
    try:
        response = requests.get(QUESTION_API_URL)
        if response.status_code == 200:
            return response.json().get("questions", [])
        else:
            st.error("Failed to load questions.")
            return []
    except requests.exceptions.RequestException:
        st.error("Could not connect to backend.")
        return []

questions = fetch_questions()

# ----------------------------
# Display Questions Form
# ----------------------------
if questions:
    with st.form("psychometric_form"):
        st.write("### ✍️ Please answer all questions:")

        user_answers = {}

        for q in questions:
            qid = q["question_id"]
            question_text = q["question_text"]
            options = [q["option_a"], q["option_b"], q["option_c"], q["option_d"]]

            selected = st.radio(f"**Q{qid}.** {question_text}", options, key=f"q_{qid}")
            user_answers[str(qid)] = selected

        submitted = st.form_submit_button("✅ Submit Test")

        if submitted:
            with st.spinner("Evaluating your responses..."):
                try:
                    response = requests.post(SCORE_API_URL, json={"answers": user_answers})

                    if response.status_code == 200:
                        result = response.json()
                        score = result.get("score", 0)
                        recommendations = result.get("recommendations", [])

                        st.success(f"🧠 Your Personality Score: **{score:.2f} / 100**")
                        st.markdown("### 🎓 Top Career Matches Based on Your Personality")

                        if recommendations:
                            for i, role in enumerate(recommendations, 1):
                                st.markdown(f"{i}. **{role}**")
                        else:
                            st.warning("No recommendations found. Try retaking the test.")
                    else:
                        st.error("❌ Server error while scoring test.")
                except requests.exceptions.RequestException:
                    st.error("⚠️ Could not connect to scoring server.")
else:
    st.warning("📭 No questions available at the moment. Please try again later.")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("🧠 Psychometric Evaluation powered by FastAPI + Streamlit + XGBoost")
