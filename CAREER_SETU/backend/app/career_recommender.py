from typing import List, Dict, Any
from .models import JobRole
from .skill_gap_analyzer import SkillGapAnalyzer

class CareerRecommender:
    def __init__(self, job_roles: List[JobRole]):
        self.job_roles = job_roles
        self.analyzer = SkillGapAnalyzer()

    def recommend(self, user_skills: List[str]) -> List[Dict[str, Any]]:
        recommendations = []
        
        for role in self.job_roles:
            analysis = self.analyzer.analyze_gap(user_skills, role.requiredSkills)
            recommendations.append({
                "role_id": role.id,
                "title": role.title,
                "match_score": analysis["readiness_score"],
                "matching_skills": analysis["matching_skills"],
                "missing_skills": analysis["missing_skills"],
                "salary": role.avgSalary,
                "demand": role.demandLevel,
                "growth": role.growth
            })
            
        # Sort by match score descending
        recommendations.sort(key=lambda x: x["match_score"], reverse=True)
        return recommendations[:5] # Return top 5
