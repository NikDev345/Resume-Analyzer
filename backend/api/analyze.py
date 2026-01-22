from fastapi import APIRouter, UploadFile, File, Form
from services.parser import extract_text
from services.section_detector import detect_sections
from services.skill_extractor import extract_skills
from services.scorer import score_resume
from services.jd_matcher import match_resume_to_jd

router = APIRouter()

@router.post("/resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    text = extract_text(file)
    sections = detect_sections(text)
    skills = extract_skills(text)
    score = score_resume(sections, skills)

    jd_result = {}
    if job_description.strip():
        jd_result = match_resume_to_jd(skills, job_description)

    return {
        "sections_found": list(sections.keys()),
        "skills": skills,
        "resume_score": score,
        "job_match": jd_result
    }
