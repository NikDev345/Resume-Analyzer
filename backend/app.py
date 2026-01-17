from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# -------------------------------
# SKILL DATABASE
# -------------------------------
JOB_SKILLS = {
    "data scientist": [
        "python",
        "sql",
        "machine learning",
        "statistics",
        "pandas",
        "numpy"
    ],
    "web developer": [
        "html",
        "css",
        "javascript",
        "react",
        "api"
    ],
    "teacher": [
        "communication",
        "lesson planning",
        "classroom management",
        "subject knowledge",
        "patience"
    ],
    "actor": [
        "acting",
        "improvisation",
        "script analysis",
        "character development",
        "voice modulation"
    ],
    "software engineer": [
        "java",
        "c++",
        "data structures",
        "algorithms",
        "system design"
    ]
}

# -------------------------------
# ANALYZE ROUTE
# -------------------------------
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    # ---- SAFETY CHECKS ----
    if not data or "resume" not in data or "role" not in data:
        return jsonify({"error": "Invalid request"}), 400

    # ---- NORMALIZATION (CRITICAL FIX) ----
    resume_text = (
        data["resume"]
        .lower()
        .replace(",", " ")
        .replace("\n", " ")
        .replace(".", " ")
    )

    role = data["role"].lower().strip()

    required_skills = JOB_SKILLS.get(role, [])

    # ---- ROLE NOT FOUND ----
    if not required_skills:
        return jsonify({
            "score": 0,
            "matched_skills": [],
            "missing_skills": [],
            "message": "Role not recognized. Please use a valid role."
        })

    # ---- MATCHING LOGIC ----
    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill in resume_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    # ---- SCORE CALCULATION ----
    score = int((len(matched_skills) / len(required_skills)) * 100)

    # ---- RESPONSE ----
    return jsonify({
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    })


# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
