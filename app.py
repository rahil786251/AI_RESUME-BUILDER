import streamlit as st
from resume_generator import generate_resume_text
from resume_to_pdf import generate_pdf

st.title("📄 Simple Resume Builder (No AI/API)")

# Input form
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (comma-separated)")
experience = st.text_area("Work Experience")
education = st.text_area("Educational Background")

# Generate button
if st.button("Generate Resume"):
    resume_text = generate_resume_text(name, email, phone, summary, skills, experience, education)
    st.text_area("Formatted Resume", resume_text, height=400)
    
    pdf = generate_pdf(resume_text)
    st.download_button("Download as PDF", pdf, file_name="resume.pdf")
