from typing import List, Dict, Any
import random

class InterviewEngine:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        # For mock/demo questions
        self.mock_questions = [
            {"role": "Full Stack Developer", "q": "Explain the difference between REST and GraphQL APIs.", "a": "REST uses fixed endpoints, GraphQL uses single endpoint with query flexibility."},
            {"role": "Data Scientist", "q": "What is the bias-variance tradeoff?", "a": "Bias is underfitting error, variance is overfitting error. Goal is to minimize both."},
            {"role": "General", "q": "Tell me about a challenging project you worked on.", "a": "Use STAR method: Situation, Task, Action, Result."}
        ]

    def get_questions(self, role: str) -> List[Dict[str, str]]:
        # Filter questions by role
        relevant = [q for q in self.mock_questions if role in q["role"] or q["role"] == "General"]
        random.shuffle(relevant)
        return relevant[:5]

    def evaluate_answer(self, question: str, answer: str) -> Dict[str, Any]:
        # In a real app, use LLM to evaluate
        score = random.randint(60, 95)
        feedback = "Excellent answer!" if score > 85 else "Good job, but you could add more technical details." if score > 70 else "Consider covering the fundamentals of this topic more clearly."
        
        return {
            "score": score,
            "feedback": feedback
        }
