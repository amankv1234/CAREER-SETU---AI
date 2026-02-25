from typing import List, Dict, Any

class RoadmapGenerator:
    def __init__(self, courses: List[Dict[str, Any]]):
        self.courses = courses

    def generate(self, missing_skills: List[str]) -> List[Dict[str, Any]]:
        # Simple 3-phase roadmap generator
        if not missing_skills:
            return []
            
        third = max(1, len(missing_skills) // 3)
        
        phases = [
            {
                "title": "Phase 1: Foundation (Days 1-30)",
                "skills": missing_skills[:third],
                "goals": ["Complete fundamentals", "Build 1 mini project"],
                "courses": self._get_courses_for_skills(missing_skills[:third])
            },
            {
                "title": "Phase 2: Intermediate (Days 31-60)",
                "skills": missing_skills[third:third*2],
                "goals": ["Deep dive into core concepts", "Build 2 real projects"],
                "courses": self._get_courses_for_skills(missing_skills[third:third*2])
            },
            {
                "title": "Phase 3: Advanced (Days 61-90)",
                "skills": missing_skills[third*2:],
                "goals": ["Advanced mastery", "Mock interviews", "Job applications"],
                "courses": self._get_courses_for_skills(missing_skills[third*2:])
            }
        ]
        
        return [p for p in phases if p["skills"]] # Return only phases with skills

    def _get_courses_for_skills(self, skills: List[str]) -> List[Dict[str, Any]]:
        matched_courses = []
        for skill in skills:
            # Find a course that matches the skill
            for course in self.courses:
                if skill.lower() in course["skill"].lower() or course["skill"].lower() in skill.lower():
                    matched_courses.append(course)
                    break
        return matched_courses
