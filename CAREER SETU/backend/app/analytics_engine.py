from typing import List, Dict, Any

class AnalyticsEngine:
    def __init__(self, district_data: List[Dict[str, Any]]):
        self.data = district_data

    def get_overview(self) -> Dict[str, Any]:
        total_workers = sum(d["totalWorkers"] for d in self.data)
        total_trained = sum(d["trainedWorkers"] for d in self.data)
        total_placed = sum(d["placedWorkers"] for d in self.data)
        
        return {
            "totalWorkers": total_workers,
            "totalTrained": total_trained,
            "totalPlaced": total_placed,
            "placementRate": round((total_placed / total_trained * 100), 1) if total_trained else 0,
            "districtsCovered": len(self.data),
            "topSkillGaps": ["AI/ML", "Cloud Computing", "Cybersecurity", "Data Analysis"] # Mock
        }

    def get_district_stats(self, state: str = None) -> List[Dict[str, Any]]:
        if state:
            return [d for d in self.data if d["state"] == state]
        return self.data
