from pydantic import BaseModel
from typing import List, Optional

class UserProfile(BaseModel):
    name: str
    email: str
    location: str
    education: str
    skills: List[str]
    interests: List[str]
    bio: Optional[str] = None

class JobRole(BaseModel):
    id: str
    title: str
    category: str
    requiredSkills: List[str]
    avgSalary: str
    demandLevel: str
    growth: str
    description: str

class ResumeAnalysis(BaseModel):
    atsScore: int
    keywordMatch: int
    extractedSkills: List[str]
    missingKeywords: List[str]
    improvements: List[str]

class SkillGapReport(BaseModel):
    matching_skills: List[str]
    missing_skills: List[str]
    readiness_score: float
    status: str
