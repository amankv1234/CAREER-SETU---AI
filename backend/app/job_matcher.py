from typing import List, Dict, Any

class JobMatcher:
    def __init__(self, job_listings: List[Dict[str, Any]]):
        self.listings = job_listings

    def match(self, user_skills: List[str], location: str = None) -> List[Dict[str, Any]]:
        user_skills_set = set(s.lower() for s in user_skills)
        matches = []
        
        for job in self.listings:
            job_skills_set = set(s.lower() for s in job["skills"])
            # Calculate intersection
            common = user_skills_set.intersection(job_skills_set)
            match_score = (len(common) / len(job_skills_set)) * 100 if job_skills_set else 0
            
            # Simple location filtering if provided
            location_match = True
            if location and location.lower() not in job["location"].lower() and location.lower() not in job.get("state", "").lower():
                location_match = False
                
            if match_score > 30 and location_match: # 30% threshold for match
                matches.append({
                    **job,
                    "match_score": round(match_score, 1)
                })
                
        matches.sort(key=lambda x: x["match_score"], reverse=True)
        return matches
