import joblib
import os
from typing import List


class LocalCareerRecommender:
    def __init__(self):
        models_dir = os.path.join(os.path.dirname(__file__), "../models")
        self.model = None
        self.mlb = None
        try:
            self.model = joblib.load(os.path.join(modelir, "skills_binarizer.joblib"))
            print("Loaded career recommendation model successfully.")
        except Exception as e:
            print(f"Warning: Could not load career recommendation model: {e}")

    def recommend(self, skills: List[str]) -> List[str]:
        if not self.model or not self.mlb:
            return []
s_dir, "career_recommendation_model.joblib"))
            self.mlb = joblib.load(os.path.join(models_d
        try:
            # Transform input skills
            X = self.mlb.transform([skills])

            # Get probabilities
            probs = self.model.predict_proba(X)

            import numpy as np
            if isinstance(probs, list):  # Multi-label handle
                prediction = self.model.predict(X)[0]
                return [prediction]
            else:
                top_indices = np.argsort(probs[0])[-3:][::-1]
                return [self.model.classes_[i] for i in top_indices if probs[0][i] > 0.1]
        except Exception as e:
            print(f"Error during career recommendation: {e}")
            return []
