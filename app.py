import streamlit as st
from resume_parser import extract_text_from_pdf
from model import get_match_score

st.title("AI Resume Screening System")

uploaded_file = st.file_uploader("Upload Resume", type="pdf")
job_desc = st.text_area("Enter Job Description")

if uploaded_file and job_desc:
    resume_text = extract_text_from_pdf(uploaded_file)
    score = get_match_score(resume_text, job_desc)

    st.subheader(f"Match Score: {score}%")

    if score > 70:
        st.success("Good Match")
    elif score > 40:
        st.warning("Average Match")
    else:
        st.error("Low Match")