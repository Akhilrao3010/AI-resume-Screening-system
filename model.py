from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_match_score(resume_text, job_desc):
    embeddings = model.encode([resume_text, job_desc])

    score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )

    return round(score[0][0] * 100, 2)