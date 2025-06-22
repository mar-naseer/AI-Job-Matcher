
# 🤖 AI Job Matching Assistant

A lightweight AI-powered tool to check how well your resume matches a job description, identify missing skills, and generate a personalized cover letter — all in one simple app.

---

## 🔍 Use Case

**Tired of not knowing whether your resume fits a job role?**  
This app helps job seekers, students, and freelancers quickly:

- ✅ Compare Resume with Job Description (PDF/DOCX)
- ✅ Get a Match Score using ML-based semantic similarity
- ✅ Find Missing Skills from JD
- ✅ Auto-generate a tailored Cover Letter (Free, no OpenAI required)

---

## ⚙️ Features

| Feature | Description |
|--------|-------------|
| 🧾 Resume + JD Upload | Accepts `.pdf` and `.docx` files |
| 🧠 Match Scoring | Uses `sentence-transformers` (MiniLM) + cosine similarity |
| 🔍 Missing Skill Detection | Highlights up to 10 missing keywords from JD |
| ✍️ Cover Letter Generator | Rule-based or OpenAI GPT (optional) |
| 🖥️ Streamlit UI | Clean and minimal web app |

---

## 📦 Tech Stack

- Python 3
- Streamlit
- sentence-transformers (`all-MiniLM-L6-v2`)
- pdfplumber + docx2txt
- scikit-learn
- (Optional) OpenAI API for GPT-based cover letters

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/ai-job-matcher.git
cd ai-job-matcher

# 2. Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
