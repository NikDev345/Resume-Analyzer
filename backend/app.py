from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

JOB_SKILLS = {
    "data scientist": [
        "python", "sql", "machine learning", "statistics", "pandas", "numpy"
    ],
    "web developer": [
        "html", "css", "javascript", "react", "api"
    ],
    "teacher": [
        "communication", "lesson planning", "classroom management",
        "subject knowledge", "patience"
    ],
    "actor": [
        "acting", "improvisation", "script analysis",
        "character development", "voice modulation"
    ],
    "software engineer": [
        "java", "c++", "data structures", "algorithms", "system design"
    ]
}

EXPECTED_SECTIONS = [
    "education", "experience", "skills", "projects", "certification"
]

ATS_UNFRIENDLY_SYMBOLS = ["★", "●", "▪", "■", "|", "✓"]


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json


    if not data or "resume" not in data or "role" not in data:
        return jsonify({"error": "Invalid request"}), 400

    raw_resume = data["resume"]

    resume_text = (
        raw_resume.lower()
        .replace(",", " ")
        .replace("\n", " ")
        .replace(".", " ")
    )

    role = data["role"].lower().strip()
    required_skills = JOB_SKILLS.get(role, [])

    if not required_skills:
        return jsonify({
            "score": 0,
            "matched_skills": [],
            "missing_skills": [],
            "message": "Role not recognized. Please use a valid role."
        })

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill in resume_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    skill_score = int((len(matched_skills) / len(required_skills)) * 100)


    ats_score = 0
    issues = []
    tips = []

    # 1. Keyword Density (40%)
    keyword_hits = sum(resume_text.count(skill) for skill in matched_skills)
    if keyword_hits >= len(required_skills) * 2:
        ats_score += 40
    else:
        ats_score += int((keyword_hits / (len(required_skills) * 2)) * 40)
        issues.append("Low keyword repetition for target role")
        tips.append("Repeat core skills naturally 2–3 times")

    section_hits = sum(1 for sec in EXPECTED_SECTIONS if sec in resume_text)
    structure_score = int((section_hits / len(EXPECTED_SECTIONS)) * 25)
    ats_score += structure_score

    if section_hits < len(EXPECTED_SECTIONS):
        issues.append("Missing important resume sections")
        tips.append("Add sections like Education, Skills, Projects, Certifications")

   
    symbol_found = any(sym in raw_resume for sym in ATS_UNFRIENDLY_SYMBOLS)
    if symbol_found:
        issues.append("ATS-unfriendly symbols detected")
        tips.append("Avoid icons, tables, symbols, and fancy bullets")
    else:
        ats_score += 20

   
    word_count = len(raw_resume.split())
    if 300 <= word_count <= 900:
        ats_score += 15
    else:
        issues.append("Resume length not optimal")
        tips.append("Keep resume between 1–2 pages (300–900 words)")


    if ats_score >= 80:
        verdict = "Excellent – ATS friendly"
    elif ats_score >= 60:
        verdict = "Good – likely to pass ATS"
    else:
        verdict = "Poor – high ATS rejection risk"

    return jsonify({
        "skill_match_score": skill_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "ats_score": ats_score,
        "ats_verdict": verdict,
        "issues_found": issues,
        "improvement_tips": tips
    })


if __name__ == "__main__":
    app.run(debug=True)
