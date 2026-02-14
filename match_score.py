from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load transformer model once (fast & light)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Clean text by removing special characters, lowering case
def clean_text(text):
    return re.sub(r'\W+', ' ', text.lower())


# Calculate semantic similarity score
def calculate_match_score(resume_text, jd_text):
    resume_embedding = model.encode([clean_text(resume_text)])
    jd_embedding = model.encode([clean_text(jd_text)])
    similarity = cosine_similarity(resume_embedding, jd_embedding)[0][0]
    return similarity * 100  # return score as percentage

# Basic skill gap finder (keywords not in resume)
def get_missing_skills(resume_text, jd_text):
    resume_words = set(clean_text(resume_text).split())
    jd_words = set(clean_text(jd_text).split())
    important_words = [word for word in jd_words if word not in resume_words and len(word) > 4]
    return list(important_words[:10])  # return top 10 missing

