# app/frontend/Home.py

import streamlit as st
from PIL import Image

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Personalized Career Guidance System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ----------------------------
# Load assets (logo, etc.)
# ----------------------------
def load_logo():
    try:
        logo = Image.open("app/assets/logo.jpg")
        st.image(logo)
    except FileNotFoundError:
        st.warning("Logo not found. Please place it in app/assets/logo.jpg")


# ----------------------------
# Sidebar Info & Navigation
# ----------------------------
with st.sidebar:
    load_logo()
    st.title("🔍 Career Navigator")
    st.markdown("""
        Use this system to get career insights and discover your best-fit roles.

        **Navigation Pages:**
        - 📄 Resume Analyzer
        - 🧠 Skill-based Recommender
        - 📝 Career Test
        - 🤖 Career Chatbot

        ---
        ℹ️ **Current Page:** Home
    """)

    # External Links
    st.markdown("---")
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
# Main Home Page Content
# ----------------------------
def show_home():
    st.title("🎯 Personalized Career Guidance System")
    st.markdown(
        """
        Welcome to the AI-powered career guidance platform tailored to assist you in finding your ideal career path 
        based on your **skills**, **resume**, and **psychometric test**.
        """
    )

    # ------------------------
    # Section 1 - Features Overview
    # ------------------------
    st.header("✨ Key Features")
    st.markdown("""
    - 📄 **Resume Analyzer**: Upload your resume and extract matched careers.
    - 🧠 **Skill Recommender**: Input skills and get smart career suggestions.
    - 📝 **Career Test**: Evaluate yourself with a psychometric-based aptitude test.
    - 🤖 **AI Chatbot Assistant**: Interact with our chatbot for personalized advice.
    """)

    # ------------------------
    # Section 2 - How the System Works
    # ------------------------
    st.header("🚀 How It Works")
    st.markdown("""
    1. Upload your **resume** or enter your **skills** manually.
    2. Take the **career-oriented test** for personal aptitude profiling.
    3. Let the AI model **analyze** your profile and suggest best career paths.
    4. Ask the chatbot anything related to **career planning** or **learning tracks**.
    """)

    # ------------------------
    # Section 3 - System Pages Explained
    # ------------------------
    st.header("📂 System Pages")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 Resume Analyzer")
        st.markdown("""
        Upload your resume and get a list of careers that best match your extracted skills using our internal matrix.
        Works with PDF or DOCX formats.
        """)

        st.subheader("🧠 Skill-based Recommender")
        st.markdown("""
        Provide your skills, CGPA, interests, and category. Our ML model recommends the top 5 careers for you.
        """)

    with col2:
        st.subheader("📝 Career Test")
        st.markdown("""
        Take a 10-question psychometric test. The system scores and returns career tracks based on your mindset.
        """)

        st.subheader("🤖 Chat Assistant")
        st.markdown("""
        Interact with the Groke-powered chatbot for queries about career decisions, roadmaps, or learning platforms.
        """)

    # ------------------------
    # Section 4 - Final CTA
    # ------------------------
    st.markdown("---")
    st.header("🧭 Ready to Explore?")
    st.markdown("""
    Use the **sidebar navigation** to:
    - Upload your resume
    - Enter profile details
    - Take the test
    - Get AI-powered suggestions
    - Or just chat with our bot 🤖
    """)

    st.success("All systems operational. Begin your journey now!")


# ----------------------------
# Main Entry
# ----------------------------
if __name__ == "__main__":
    show_home()
