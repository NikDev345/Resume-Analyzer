from sentence_transformers import SentenceTransformer, util
from services.skill_extractor import extract_skills

model = SentenceTransformer("all-MiniLM-L6-v2")

def match_resume_to_jd(resume_skills, jd_text):
    jd_skills = extract_skills(jd_text)

    # SAFETY DEBUG
    print("JD SKILLS:", jd_skills)

    if not jd_skills:
        return {
            "match_percentage": 0,
            "matched_skills": [],
            "missing_skills": resume_skills
        }

    resume_emb = model.encode(resume_skills, convert_to_tensor=True)
    jd_emb = model.encode(jd_skills, convert_to_tensor=True)

    matched = set()

    for i, skill in enumerate(resume_skills):
        if util.cos_sim(resume_emb[i], jd_emb).max().item() > 0.5:
            matched.add(skill)

    return {
        "match_percentage": int((len(matched) / len(resume_skills)) * 100),
        "matched_skills": sorted(matched),
        "missing_skills": sorted(set(resume_skills) - matched)
    }
