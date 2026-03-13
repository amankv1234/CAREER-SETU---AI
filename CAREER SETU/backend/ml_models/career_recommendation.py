import joblib
import os
from typing import List

class LocalCareerRecommender:
    def __init__(self):
        models_dir = os.path.join(os.path.dirname(__file__), "../models")
        self.model = joblib.load(os.path.join(models_dir, "career_recommendation_model.joblib"))
        self.mlb = joblib.load(os.path.join(models_dir, "skills_binarizer.joblib"))

    def recommend(self, skills: List[str]) -> List[str]:
        # Transform input skills
        X = self.mlb.transform([skills])
        
        # Get probabilities
        probs = self.model.predict_proba(X)
        
        # Get top classes
        # This is a bit tricky with RandomForest handle-all-classes
        # For simplicity, we'll just return the predicted class and top 2 alternatives if available
        # But using model.classes_
        
        import numpy as np
        if isinstance(probs, list): # Multi-label handle
             # Simplify for this demo
             prediction = self.model.predict(X)[0]
             return [prediction]
        else:
            top_indices = np.argsort(probs[0])[-3:][::-1]
            return [self.model.classes_[i] for i in top_indices if probs[0][i] > 0.1]
