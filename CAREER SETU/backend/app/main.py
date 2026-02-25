from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from typing import List, Dict, Any, Optional
from pydantic import BaseModel

from .skill_extractor import SkillExtractor
from .skill_gap_analyzer import SkillGapAnalyzer
from .career_recommender import CareerRecommender
from .roadmap_generator import RoadmapGenerator
from .resume_scorer import ResumeScorer
from .interview_engine import InterviewEngine
from .analytics_engine import AnalyticsEngine
from .models import UserProfile, JobRole, ResumeAnalysis, SkillGapReport

app = FastAPI(title="SkillBridge AI API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize engines
extractor = SkillExtractor()
gap_analyzer = SkillGapAnalyzer()
# Mock data for engines initialization
MOCK_ROLES = [
    JobRole(id="1", title="Full Stack Developer", category="Web Development", requiredSkills=["JavaScript", "React", "Node.js", "MongoDB"], avgSalary="₹8-20 LPA", demandLevel="High", growth="+25%", description="Build web apps"),
    JobRole(id="2", title="Data Scientist", category="Data Science", requiredSkills=["Python", "Pandas", "Scikit-learn", "TensorFlow"], avgSalary="₹10-30 LPA", demandLevel="High", growth="+35%", description="Analyze data")
]
MOCK_COURSES = [
    {"title": "Python for Everybody", "skill": "Python", "platform": "Coursera", "url": "https://coursera.org"},
    {"title": "React Masterclass", "skill": "React", "platform": "Udemy", "url": "https://udemy.com"}
]
MOCK_DISTRICTS = [
    {"state": "Karnataka", "district": "Bangalore", "totalWorkers": 450000, "trainedWorkers": 180000, "placedWorkers": 145000, "topSkillGaps": ["AI", "Cloud"], "demandRoles": ["Dev"]}
]

career_recommender = CareerRecommender(MOCK_ROLES)
roadmap_generator = RoadmapGenerator(MOCK_COURSES)
resume_scorer = ResumeScorer() # Add GEMINI_API_KEY if available
interview_engine = InterviewEngine()
analytics_engine = AnalyticsEngine(MOCK_DISTRICTS)

@app.get("/")
async def root():
    return {"message": "Welcome to SkillBridge AI API"}

# Auth & Profile
@app.post("/api/auth/register")
async def register(profile: UserProfile):
    # In real app, save to DB
    return {"message": "User registered successfully", "user": profile}

@app.post("/api/auth/login")
async def login(credentials: Dict[str, str]):
    return {"access_token": "mock_token", "token_type": "bearer"}

@app.get("/api/profile")
async def get_profile():
    return {
        "name": "Sachin Sharma",
        "email": "sachin@example.com",
        "skills": ["React", "JavaScript", "Python"],
        "location": "Bangalore"
    }

# Core Features
@app.post("/api/resume/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")
    analysis = await resume_scorer.score_resume(text)
    return analysis

@app.post("/api/skills/gap")
async def analyze_skill_gap(data: Dict[str, Any]):
    user_skills = data.get("user_skills", [])
    target_role_id = data.get("role_id")
    
    role = next((r for r in MOCK_ROLES if r.id == target_role_id), MOCK_ROLES[0])
    report = gap_analyzer.analyze_gap(user_skills, role.requiredSkills)
    return report

@app.get("/api/career/recommend")
async def recommend_careers(skills: str):
    skill_list = skills.split(",")
    return career_recommender.recommend(skill_list)

@app.get("/api/roadmap/{role_id}")
async def get_roadmap(role_id: str):
    role = next((r for r in MOCK_ROLES if r.id == role_id), MOCK_ROLES[0])
    # For demo, assuming these are missing skills
    return roadmap_generator.generate(role.requiredSkills)

@app.get("/api/jobs")
async def get_jobs(location: Optional[str] = None):
    # Return mock jobs from matcher
    from .job_matcher import JobMatcher
    MOCK_JOBS = [{"title": "React Dev", "company": "Tech Corp", "location": "Bangalore", "skills": ["React", "JS"]}]
    matcher = JobMatcher(MOCK_JOBS)
    return matcher.match(["React"], location)

@app.post("/api/interview/start")
async def start_interview(role_id: str):
    role = next((r for r in MOCK_ROLES if r.id == role_id), MOCK_ROLES[0])
    return interview_engine.get_questions(role.title)

@app.post("/api/interview/evaluate")
async def evaluate_answer(data: Dict[str, str]):
    return interview_engine.evaluate_answer(data.get("question", ""), data.get("answer", ""))

@app.get("/api/analytics/overview")
async def get_analytics_overview():
    return analytics_engine.get_overview()

@app.get("/api/analytics/districts")
async def get_district_analytics(state: Optional[str] = None):
    return analytics_engine.get_district_stats(state)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
