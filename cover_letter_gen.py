def generate_cover_letter(resume_text, jd_text):
    # Basic keyword extract from job description
    keywords = [word for word in jd_text.split() if word.lower() in resume_text.lower()]
    keywords = list(set(keywords))[:5]

    letter = f"""
Dear Hiring Manager,

I am writing to express my interest in the role you've described. With a background that aligns well with your requirements — including {', '.join(keywords)} — I believe I can contribute meaningfully to your team.

My experiences and skills closely match the job description, and I am eager to bring dedication, adaptability, and a problem-solving mindset to your organization.

Thank you for considering my application. I look forward to the opportunity to discuss how I can add value to your team.

Sincerely,  
Your Name
"""
    return letter
