# app/frontend/pages/1_📄_Resume_Parser.py

import streamlit as st
import requests
import os

# Backend API endpoint for resume parsing
API_URL = "http://localhost:8000/resume/upload"

# ----------------------------
# Streamlit Page Config
# ----------------------------
st.set_page_config(page_title="📄 Resume Parser", page_icon="📄")

# ----------------------------
# Sidebar Navigation
# ----------------------------
st.sidebar.title("🔍 Resume Parser")
st.sidebar.markdown("**Page:** Resume Parser")
st.sidebar.info(
    "This tool analyzes resumes (PDF/DOCX), extracts relevant skills using NLP, "
    "and recommends suitable career roles using a Machine Learning model."
)
st.sidebar.success("Status: Active")

# Sidebar Buttons
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
# Title & Overview
# ----------------------------
st.title("📄 Resume Parser and Career Recommender")
st.markdown(
    """
    Welcome to the **Resume Analysis Tool** — an AI-powered module that:
    - 🧠 Parses uploaded resumes using NLP
    - 🧪 Extracts key skills from the content
    - 🎯 Suggests career paths that match your expertise

    > Supported file types: **PDF, DOCX**
    """
)

# ----------------------------
# Step 1: Upload Resume
# ----------------------------
st.subheader("📤 Step 1: Upload Your Resume")
uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

if uploaded_file:
    file_name = uploaded_file.name
    file_ext = os.path.splitext(file_name)[1].lower()

    if file_ext not in [".pdf", ".docx"]:
        st.error("❌ Invalid format. Please upload a PDF or DOCX.")
    else:
        st.success(f"✅ Uploaded: `{file_name}`")

        # ----------------------------
        # Step 2: Analyze Resume
        # ----------------------------
        st.subheader("🔎 Step 2: Analyze Resume")
        if st.button("🚀 Start Analysis"):
            with st.spinner("Analyzing your resume..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                    response = requests.post(API_URL, files=files)

                    if response.status_code == 200:
                        result = response.json()
                        extracted_skills = result.get("extracted_skills", [])
                        recommendations = []

                        # Send extracted skills for recommendation
                        if extracted_skills:
                            analysis_resp = requests.post(
                                f"{API_URL}/analyze_resume/",
                                json={"extracted_skills": extracted_skills}
                            )
                            if analysis_resp.status_code == 200:
                                analysis_result = analysis_resp.json()
                                recommendations = analysis_result.get("matched_careers", [])

                        # ----------------------------
                        # Step 3: Display Results
                        # ----------------------------
                        st.subheader("🧠 Extracted Skills")
                        if extracted_skills:
                            st.success("**" + ", ".join(extracted_skills) + "**")
                        else:
                            st.warning("No clear skills were identified from your resume.")

                        st.subheader("🎯 Recommended Career Roles")
                        if recommendations:
                            for i, role in enumerate(recommendations, start=1):
                                st.markdown(f"**{i}. {role}**")
                        else:
                            st.info("No direct career matches found. Try refining your resume.")

                    else:
                        st.error("⚠️ Resume analysis failed. Please check the backend API.")

                except requests.exceptions.ConnectionError:
                    st.error("❌ Could not connect to backend. Ensure FastAPI server is running.")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("⚙️ System powered by **spaCy**, **PyMuPDF**, **FastAPI**, and **scikit-learn**.")
