import pdfplumber
import docx2txt

def extract_jd_text(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        with pdfplumber.open(uploaded_file) as pdf:
            text = ""
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
            return text
    elif uploaded_file.name.endswith(".docx"):
        return docx2txt.process(uploaded_file)
    else:
        return "Unsupported file format"
