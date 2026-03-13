from sentence_transformers import SentenceTransformer, util
import os

class LocalJobMatcher:
    def __init__(self):
        # We load a small model for efficiency
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def match(self, resume_text: str, job_descriptions: list):
        resume_embedding = self.model.encode(resume_text, convert_to_tensor=True)
        job_embeddings = self.model.encode(job_descriptions, convert_to_tensor=True)
        
        cosine_scores = util.cos_sim(resume_embedding, job_embeddings)[0]
        
        # Sort by score
        results = []
        for i, score in enumerate(cosine_scores):
            results.append({
                "index": i,
                "score": float(score)
            })
            
        return sorted(results, key=lambda x: x['score'], reverse=True)
