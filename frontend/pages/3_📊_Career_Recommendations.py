# app/frontend/pages/3_📊_Career_Recommendations.py

import streamlit as st
import requests
import io

# ----------------------------
# Sidebar Content
# ----------------------------
st.sidebar.title("🔍 System Overview")
st.sidebar.info("""
This module uses resume parsing and ML to analyze your skills and provide career recommendations.
""")

st.sidebar.markdown("---")
st.sidebar.subheader("📑 Current Page")
st.sidebar.markdown("""
**Career Recommendations from Resume**

- Upload your resume.
- Extracted skills will be displayed.
- Career suggestions based on skill-match ML model.
""")


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


# ----------------------------
# Main Page Title and Description
# ----------------------------
st.title("📊 Career Recommendations Based on Resume")
st.markdown("""
Upload your **resume (PDF or DOCX)** to get **AI-driven career suggestions** based on your extracted skills.

Our model uses NLP and ML to match your capabilities with trending job roles.
""")

# ----------------------------
# Backend API Endpoint
# ----------------------------
UPLOAD_API_URL = "http://localhost:8000/resume/upload"

# ----------------------------
# File Upload and Analysis
# ----------------------------
uploaded_file = st.file_uploader("📄 Upload your Resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    st.success(f"✅ Uploaded: `{uploaded_file.name}`")

    if st.button("🚀 Analyze Resume"):
        with st.spinner("🔍 Analyzing your resume..."):

            file_bytes = uploaded_file.read()

            try:
                response = requests.post(
                    UPLOAD_API_URL,
                    files={"file": (uploaded_file.name, file_bytes)},
                    timeout=30
                )

                if response.status_code == 200:
                    data = response.json()
                    skills = data.get("skills", [])
                    recommendations = data.get("recommendations", [])

                    st.markdown("## ✅ Extracted Skills")
                    if skills:
                        st.markdown(", ".join(f"`{skill}`" for skill in skills))
                    else:
                        st.warning("No skills were detected in your resume.")

                    st.markdown("## 🎯 Recommended Careers")
                    if recommendations:
                        for i, job in enumerate(recommendations, start=1):
                            st.markdown(f"**{i}. {job}**")
                    else:
                        st.info("Try uploading a more detailed resume to get better recommendations.")

                else:
                    st.error(f"❌ Failed to process resume. Status code: {response.status_code}")

            except requests.exceptions.RequestException as e:
                st.error(f"🔌 Backend Error: {e}")

else:
    st.warning("📤 Please upload a resume to continue.")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("🔧 Built with FastAPI + Streamlit | 🧠 AI by Amal Prasad Trivedi")