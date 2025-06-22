import streamlit as st
from resume_parser import extract_resume_text
from jd_parser import extract_jd_text
from match_score import calculate_match_score, get_missing_skills
from cover_letter_gen import generate_cover_letter

# Page setup
st.set_page_config(page_title="AI Job Matcher", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# App title and description
st.title("🤖 AI Job Matching Assistant")
st.markdown("Boost your chances of landing the job with AI-powered resume matching & instant cover letter generation.")

# File upload section
with st.container():
    st.markdown("### 📤 Upload Files")
    resume_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
    jd_file = st.file_uploader("Upload the Job Description (PDF or DOCX)", type=["pdf", "docx"])

# Processing section
if resume_file and jd_file:
    with st.spinner("🔍 Analyzing your documents..."):
        resume_text = extract_resume_text(resume_file)
        jd_text = extract_jd_text(jd_file)

        score = calculate_match_score(resume_text, jd_text)
        gaps = get_missing_skills(resume_text, jd_text)

    st.markdown("---")
    st.subheader("📊 Match Score")
    st.success(f"✅ Your resume matches {round(score, 2)}% with the job description.")
    st.progress(int(score))

    st.subheader("🛠️ Missing Skills")
    if gaps:
        st.warning("Here are some suggested skills to add:")
        st.write(", ".join(gaps))
    else:
        st.info("No major gaps found. Looks great!")

    if st.button("✍️ Generate Cover Letter"):
        with st.spinner("💌 Writing your cover letter..."):
            letter = generate_cover_letter(resume_text, jd_text)
        st.subheader("📩 Personalized Cover Letter")
        st.code(letter, language='markdown')

# Footer
st.markdown("---")
st.markdown("<center><small>Made with 💖 by Naseer & Ibrahim @ Code For India Hackathon 2025</small></center>", unsafe_allow_html=True)
