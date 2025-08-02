# app/frontend/pages/4_📚_Learning_Resources.py

import streamlit as st

# ----------------------------
# Page Setup
# ----------------------------
st.set_page_config(page_title="Learning Resources", page_icon="📚")

# Sidebar Navigation & Info
st.sidebar.title("🔍 Navigation")
st.sidebar.markdown("**Current Page:** Learning Resources")
st.sidebar.markdown("Navigate through different pages to explore:")
st.sidebar.markdown("- 🧠 Psychometric Test\n- 📊 Career Recommendations\n- 📚 Learning Resources")

st.sidebar.markdown("---")
st.sidebar.markdown("📌 **Status**: Ready to Learn!")

# Portfolio and LinkedIn Buttons

# External Links
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Connect with Developer")
st.sidebar.link_button("🌐 Portfolio", "https://amalprasadtrivediportfolio.vercel.app/")
st.sidebar.link_button("🔗 LinkedIn", "https://linkedin.com/posts/amalprasadtrivedi-aiml-engineer")

# Footer badge
st.sidebar.markdown(
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

# Main Title
st.title("📚 Learning Resources")
st.markdown("Welcome to the **Learning Resources** hub of the Personalized Career Guidance System.\nHere you'll find curated content tailored to various careers in tech and AI/ML.\nUse these resources to level up your skills based on your interests or test results.")

# ----------------------------
# Static Career Resource Mapping
# ----------------------------
career_resources = {
    "Data Scientist": [
        ("Data Science Specialization - Coursera", "https://www.coursera.org/specializations/jhu-data-science"),
        ("Kaggle Learn - Data Science", "https://www.kaggle.com/learn"),
        ("Hands-On Machine Learning - O'Reilly", "https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/")
    ],
    "Machine Learning Engineer": [
        ("Machine Learning by Andrew Ng - Coursera", "https://www.coursera.org/learn/machine-learning"),
        ("Fast.ai Practical Deep Learning", "https://course.fast.ai/"),
        ("ML Engineering Guide - Google", "https://developers.google.com/machine-learning/guides")
    ],
    "AI Researcher": [
        ("Deep Learning Specialization - Coursera", "https://www.coursera.org/specializations/deep-learning"),
        ("AI Research Papers - arXiv", "https://arxiv.org/list/cs.AI/recent"),
        ("Transformer Models - HuggingFace", "https://huggingface.co/course")
    ],
    "Backend Developer": [
        ("Backend Development - Full Stack Open", "https://fullstackopen.com/en/"),
        ("FastAPI Documentation", "https://fastapi.tiangolo.com/"),
        ("Designing Microservices", "https://martinfowler.com/articles/microservices.html")
    ],
    "NLP Engineer": [
        ("Natural Language Processing - Coursera", "https://www.coursera.org/learn/classification-vector-spaces-in-nlp"),
        ("Stanford NLP Course (CS224N)", "https://web.stanford.edu/class/cs224n/"),
        ("spaCy NLP Documentation", "https://spacy.io/")
    ],
    "Frontend Developer": [
        ("Frontend Development - FreeCodeCamp", "https://www.freecodecamp.org/learn"),
        ("JavaScript + React Crash Course", "https://scrimba.com/learn/learnreact"),
        ("Tailwind CSS Documentation", "https://tailwindcss.com/docs")
    ]
}

# ----------------------------
# Career Dropdown
# ----------------------------
st.subheader("🎯 Select a Career Track to Explore")
selected_career = st.selectbox("Choose from the list:", list(career_resources.keys()))

# ----------------------------
# Display Resources
# ----------------------------
if selected_career:
    st.markdown(f"### 📘 Recommended Resources for **{selected_career}**")
    resources = career_resources[selected_career]

    for title, link in resources:
        st.markdown(f"- [{title}]({link})")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("📚 Keep learning. Stay curious! | Built with ❤️ by Amal Prasad Trivedi")
