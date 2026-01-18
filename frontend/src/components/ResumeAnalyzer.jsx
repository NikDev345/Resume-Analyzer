import { useState } from "react";
import "./ResumeAnalyzer.css";

export default function ResumeAnalyzer() {
  const [resume, setResume] = useState("");
  const [role, setRole] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeResume = async () => {
    if (!resume || !role) return;

    setLoading(true);
    try {
      const res = await fetch("http://localhost:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ resume, role }),
      });

      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div className="analyzer-page">
      <div className="analyzer-card">
        <h2>Resume Analysis</h2>
        <p className="subtitle">
          Paste your resume and choose a target role to evaluate your job readiness.
        </p>

        <textarea
          placeholder="Paste your resume text here..."
          value={resume}
          onChange={(e) => setResume(e.target.value)}
        />

        <input
          type="text"
          placeholder="Target Role (e.g. Data Scientist)"
          value={role}
          onChange={(e) => setRole(e.target.value)}
        />

        <button onClick={analyzeResume} disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

        {result && (
          <div className="result-section">
            {/* SKILL MATCH SCORE */}
            <div className="score">
              <span>{result.skill_match_score}%</span>
              <p>Skill Match Score</p>
            </div>

            {/* ATS SCORE */}
            <div className="score ats-score">
              <span>{result.ats_score}%</span>
              <p>ATS Compatibility</p>
            </div>

            {/* SKILLS */}
            <div className="skills-grid">
              <div className="skill-card matched-card">
                <h4>Matched Skills ({result.matched_skills.length})</h4>
                <div className="skill-pills">
                  {result.matched_skills.length > 0 ? (
                    result.matched_skills.map((s, i) => (
                      <span key={i} className="pill matched-pill">
                        {s}
                      </span>
                    ))
                  ) : (
                    <p className="empty">No matched skills</p>
                  )}
                </div>
              </div>

              <div className="skill-card missing-card">
                <h4>Missing Skills ({result.missing_skills.length})</h4>
                <div className="skill-pills">
                  {result.missing_skills.length > 0 ? (
                    result.missing_skills.map((s, i) => (
                      <span key={i} className="pill missing-pill">
                        {s}
                      </span>
                    ))
                  ) : (
                    <p className="empty">No missing skills</p>
                  )}
                </div>
              </div>
            </div>

            {/* SKILL FIT VERDICT */}
            <div
              className={`verdict ${
                result.skill_match_score < 40
                  ? "bad"
                  : result.skill_match_score < 70
                  ? "average"
                  : "good"
              }`}
            >
              {result.skill_match_score < 40 && "❌ Poor Skill Match"}
              {result.skill_match_score >= 40 &&
                result.skill_match_score < 70 &&
                "⚠️ Average Skill Match"}
              {result.skill_match_score >= 70 && "✅ Strong Skill Match"}
            </div>

            {/* ATS VERDICT */}
            <div className="ats-verdict">
              <h4>ATS Verdict</h4>
              <p>{result.ats_verdict}</p>
            </div>

            {/* ISSUES */}
            {result.issues_found.length > 0 && (
              <div className="issues">
                <h4>Issues Detected</h4>
                <ul>
                  {result.issues_found.map((issue, i) => (
                    <li key={i}>{issue}</li>
                  ))}
                </ul>
              </div>
            )}

            {/* IMPROVEMENT TIPS */}
            {result.improvement_tips.length > 0 && (
              <div className="tips">
                <h4>Improvement Tips</h4>
                <ul>
                  {result.improvement_tips.map((tip, i) => (
                    <li key={i}>{tip}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
