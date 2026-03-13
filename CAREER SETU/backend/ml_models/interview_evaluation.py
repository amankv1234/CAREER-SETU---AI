from sentence_transformers import SentenceTransformer, util
from typing import Dict, Any

class LocalInterviewEvaluator:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def evaluate(self, user_answer: str, expected_answer: str) -> Dict[str, Any]:
        # Encode
        user_emb = self.model.encode(user_answer, convert_to_tensor=True)
        expected_emb = self.model.encode(expected_answer, convert_to_tensor=True)
        
        # Similarity
        similarity = float(util.cos_sim(user_emb, expected_emb)[0])
        score = int(similarity * 100)
        
        # Feedback logic based on similarity
        feedback = ""
        if score > 80:
            feedback = "Excellent! You covered all key points with high accuracy."
        elif score > 50:
            feedback = "Good effort. You hit some key aspects, but try to be more specific and technical."
        else:
            feedback = "Needs improvement. Your answer lacks critical details found in the ideal response."
            
        return {
            "score": score,
            "feedback": feedback,
            "similarity": round(similarity, 2)
        }
