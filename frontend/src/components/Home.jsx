import "./Home.css";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="home">
      <div className="grid-bg" />

      <div className="content">
        <h1>
          AI Resume <span>Analyzer</span>
        </h1>

        <p>
          Analyze your resume intelligently.  
          Identify skill gaps.  
          Get career-ready with clarity.
        </p>

        <button onClick={() => navigate("/analyze")}>
          Start Analysis
        </button>
      </div>
    </div>
  );
}
