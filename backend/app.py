from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

JOB_SKILLS = {
    "data scientist": ["python", "sql", "machine learning", "statistics", "pandas"],
    "web developer": ["html", "css", "javascript", "react", "api"]
}

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    resume_text = data["resume"].lower()
    role = data["role"].lower()

    required = JOB_SKILLS.get(role, [])
    matched = [s for s in required if s in resume_text]
    missing = [s for s in required if s not in resume_text]

    score = int((len(matched) / len(required)) * 100) if required else 0

    return jsonify({
        "matched_skills": matched,
        "missing_skills": missing,
        "score": score
    })

if __name__ == "__main__":
    app.run(debug=True)
