import spacy
from typing import List, Set
import json
import os

class SkillExtractor:
    def __init__(self):
        # Load spacy model
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            # Fallback if model not downloaded yet
            self.nlp = None
        
        # Load skills database
        self.skills_db = self._load_skills_db()
        self.all_skills = set()
        for category in self.skills_db.values():
            for skill in category:
                self.all_skills.add(skill.lower())

    def _load_skills_db(self):
        # Mocking the skills DB for now, in production load from JSON
        return {
            "Programming": ["Python", "JavaScript", "TypeScript", "Java", "C++", "C#", "Go", "Rust", "PHP", "Ruby", "Swift", "Kotlin"],
            "Web Development": ["React", "Next.js", "Angular", "Vue.js", "Node.js", "Express.js", "Django", "Flask", "HTML5", "CSS3", "Tailwind CSS", "Bootstrap"],
            "Data Science": ["Pandas", "NumPy", "Scikit-learn", "TensorFlow", "PyTorch", "Matplotlib", "Seaborn", "Jupyter", "R", "SAS"],
            "Cloud & DevOps": ["AWS", "Azure", "GCP", "Docker", "Kubernetes", "Jenkins", "Terraform", "CI/CD", "Linux", "Nginx"],
            "Database": ["SQL", "PostgreSQL", "MongoDB", "MySQL", "Redis", "Firebase", "Cassandra", "DynamoDB"],
            "AI/ML": ["Machine Learning", "Deep Learning", "NLP", "Computer Vision", "Generative AI", "LLMs", "Prompt Engineering", "MLOps"],
            "Design": ["Figma", "Adobe XD", "Photoshop", "Illustrator", "UI/UX Design", "Wireframing", "Prototyping"],
            "Business Skills": ["Project Management", "Agile", "Scrum", "Communication", "Leadership", "Problem Solving", "Critical Thinking", "Teamwork"],
        }

    def extract_skills(self, text: str) -> List[str]:
        if not text:
            return []
        
        found_skills = []
        text_lower = text.lower()
        
        # Simple keyword matching
        for skill in self.all_skills:
            # Check for skill as a whole word to avoid partial matches (e.g., 'C' in 'CAT')
            if f" {skill} " in f" {text_lower} " or f" {skill}," in f" {text_lower} " or f"\n{skill}" in f"\n{text_lower}":
                # Find the original case from the database
                for category in self.skills_db.values():
                    for original_skill in category:
                        if original_skill.lower() == skill:
                            found_skills.append(original_skill)
                            break
        
        return list(set(found_skills))

    def extract_from_resume(self, text: str):
        # In a real app, this would use more complex NLP (NER)
        # to distinguish between personal info, experience, and skills
        skills = self.extract_skills(text)
        return {
            "skills": skills,
            "experience_years": 0, # Placeholder
            "education": "Detected from text" # Placeholder
        }
