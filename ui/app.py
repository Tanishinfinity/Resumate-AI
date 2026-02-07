import streamlit as st
import sys
import os

# -------------------------------------------------
# Allow Streamlit to import backend from /src
# -------------------------------------------------
sys.path.append(os.path.abspath("src"))

from resume_parser import extract_text
from ats_scoring import clean_text, ats_score
from gemini_ai import analyze_resume

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="ResuMate AI",
    layout="centered"
)

# -------------------------------------------------
# UI Header
# -------------------------------------------------
st.title("📄 ResuMate AI")
st.subheader("AI-Powered Resume Analysis & Enhancement Platform")

st.markdown(
    """
    Upload your resume and paste a job description to:
    - Calculate ATS compatibility score  
    - Get AI-powered resume improvement suggestions  
    """
)

st.divider()

# -------------------------------------------------
# Resume Upload
# -------------------------------------------------
resume_file = st.file_uploader(
    "📤 Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

# -------------------------------------------------
# Job Description Input
# -------------------------------------------------
jd_text = st.text_area(
    "📝 Paste Job Description",
    height=200,
    placeholder="Paste the job description here..."
)

# -------------------------------------------------
# Analyze Button
# -------------------------------------------------
if st.button("🚀 Analyze Resume"):
    if resume_file is None:
        st.error("❌ Please upload a resume file.")
    elif jd_text.strip() == "":
        st.error("❌ Please paste a job description.")
    else:
        try:
            # -----------------------------------------
            # Save uploaded resume with correct extension
            # -----------------------------------------
            file_extension = resume_file.name.split(".")[-1].lower()
            temp_resume_path = f"temp_resume.{file_extension}"

            with open(temp_resume_path, "wb") as f:
                f.write(resume_file.read())

            # -----------------------------------------
            # Resume Parsing
            # -----------------------------------------
            resume_text = extract_text(temp_resume_path)

            # -----------------------------------------
            # ATS Scoring
            # -----------------------------------------
            clean_resume = clean_text(resume_text)
            clean_jd = clean_text(jd_text)

            score = ats_score(clean_resume, clean_jd)

            st.success(f"✅ ATS Compatibility Score: **{score}%**")

            # -----------------------------------------
            # Gemini AI Analysis
            # -----------------------------------------
            with st.spinner("🤖 Analyzing resume with AI..."):
                ai_suggestions = analyze_resume(resume_text, jd_text)

            st.subheader("✨ AI Resume Improvement Suggestions")
            st.write(ai_suggestions)

            # -----------------------------------------
            # Cleanup temp file
            # -----------------------------------------
            if os.path.exists(temp_resume_path):
                os.remove(temp_resume_path)

        except Exception as e:
            st.error("⚠️ An error occurred while processing the resume.")
            st.code(str(e))

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.divider()
st.caption("© 2025 ResuMate AI | Built with Python, NLP & Gemini AI")