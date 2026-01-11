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
        body: JSON.stringify({ resume, role })
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
          Paste your resume and choose a target role to evaluate your career readiness.
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
            <div className="score">
              <span>{result.score}%</span>
              <p>Skill Match Score</p>
            </div>

            <div className="skills">
              <div>
                <h4>Matched Skills</h4>
                <ul>
                  {result.matched_skills.map((s, i) => (
                    <li key={i} className="matched">{s}</li>
                  ))}
                </ul>
              </div>

              <div>
                <h4>Missing Skills</h4>
                <ul>
                  {result.missing_skills.map((s, i) => (
                    <li key={i} className="missing">{s}</li>
                  ))}
                </ul>
              </div>
            </div>

            <div className="verdict">
              {result.score < 40 && "❌ Needs Improvement"}
              {result.score >= 40 && result.score < 70 && "⚠️ Average Fit"}
              {result.score >= 70 && "✅ Strong Fit"}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
