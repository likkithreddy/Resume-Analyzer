from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')




def skill_overlap_score(resume_skills, jd_skills):
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    if not jd_set:
        return 0

    overlap = resume_set.intersection(jd_set)
    return len(overlap) / len(jd_set)



def category_overlap_score(resume_categories, jd_categories):
    resume_cat = set(resume_categories.keys())
    jd_cat = set(jd_categories.keys())

    if not jd_cat:
        return 0

    overlap = resume_cat.intersection(jd_cat)
    return len(overlap) / len(jd_cat)




def tfidf_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words='english')

    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    return similarity




def semantic_similarity(resume_text, jd_text):
    embeddings = model.encode([resume_text, jd_text])
    sim = np.dot(embeddings[0], embeddings[1]) / (
        np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1])
    )
    return float(sim)




def compute_final_score(skill_score, category_score, tfidf_score, semantic_score):

    final = (
        0.3 * skill_score +
        0.2 * category_score +
        0.25 * tfidf_score +
        0.25 * semantic_score
    )

    return round(final * 100, 2)
