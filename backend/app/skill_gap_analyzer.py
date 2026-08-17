from typing import List, Dict, Any
from .skill_extractor import SkillExtractor

class SkillGapAnalyzer:
    def __init__(self):
        self.extractor = SkillExtractor()

    def analyze_gap(self, user_skills: List[str], target_role_skills: List[str]) -> Dict[str, Any]:
        user_skills_set = set(s.lower() for s in user_skills)
        target_skills_set = set(s.lower() for s in target_role_skills)
        
        matching = []
        missing = []
        
        # Match user skills to target role requirements
        for skill in target_role_skills:
            if skill.lower() in user_skills_set:
                matching.append(skill)
            else:
                missing.append(skill)
                
        readiness_score = (len(matching) / len(target_role_skills)) * 100 if target_role_skills else 0
        
        return {
            "matching_skills": matching,
            "missing_skills": missing,
            "readiness_score": round(readiness_score, 1),
            "status": "Ready" if readiness_score > 80 else "Improving" if readiness_score > 50 else "Gap Identified"
        }
