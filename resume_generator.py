def generate_resume_text(name, email, phone, summary, skills, experience, education):
    skills_list = [skill.strip() for skill in skills.split(",")]

    resume = f"""
{name.upper()}
Email: {email} | Phone: {phone}

SUMMARY
{summary}

SKILLS
{', '.join(skills_list)}

EXPERIENCE
{experience}

EDUCATION
{education}
"""
    return resume.strip()
