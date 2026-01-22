🚀 Resume Analyzer — Intelligent ATS-Style Resume Scoring System
<p align="center"> <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=900&color=36BCF7&center=true&vCenter=true&width=900&lines=FastAPI+%7C+NLP+Backend+System;ATS-Style+Resume+Parsing+and+Scoring;PDF+%26+DOCX+Resume+Analysis;Built+for+Scalability+and+Future+AI+Extensions" /> </p> <p align="center"> <b>An intelligent backend system that parses resumes, extracts structured insights, and generates ATS-style resume scores using NLP.</b> </p>
🧠 Project Overview

Resume Analyzer is a backend-driven NLP system designed to analyze resumes the way real Applicant Tracking Systems (ATS) do.

Unlike simple keyword matchers, this system focuses on:

Resume structure

Skill normalization

Section depth

Realistic scoring, not inflated results

The architecture is intentionally designed to support future AI/ML enhancements such as semantic job matching and automated resume feedback.

✨ Live System Flow (Animated via Mermaid)
flowchart LR
    subgraph INPUT["📄 Input Layer"]
        U[👤 User]
        F[📎 Resume<br/>(PDF / DOCX)]
    end

    subgraph NLP["🧠 NLP Engine"]
        P[🔍 Text<br/>Extraction]
        S[🧩 Section<br/>Detection]
        K[🛠️ Skill<br/>Normalization]
    end

    subgraph ATS["📊 ATS Logic"]
        R[⚖️ Resume<br/>Scoring]
    end

    O[📦 Structured JSON Output]

    U --> F --> P
    P --> S --> K --> R --> O

⚙️ Backend Interaction (Sequence View)
sequenceDiagram
    participant U as User
    participant A as FastAPI API
    participant N as NLP Engine

    U->>A: Upload Resume (PDF/DOCX)
    A->>N: Extract Text
    N->>N: Detect Sections
    N->>N: Normalize Skills
    N->>A: Compute ATS Score
    A->>U: Return JSON Result

🔥 Key Features
📄 Resume Parsing

Supports PDF and DOCX

Clean text extraction

Handles real-world resume formatting

🧩 Section Detection

Automatically identifies:

Experience

Skills

Projects

Education

🛠️ Skill Extraction & Normalization

Canonical skill mapping

Handles variations:

ML → Machine Learning

DL → Deep Learning

Avoids duplicate & noisy skills

📊 ATS-Style Resume Scoring

Score range: 0–100

Based on:

Section presence

Section depth

Skill diversity

Prevents artificial score inflation

⚙️ System Status (Live-Style)
🟢 Resume Parsing        ▓▓▓▓▓▓▓▓▓▓ 100%
🟢 Section Detection     ▓▓▓▓▓▓▓▓▓▓ 100%
🟡 Skill Normalization   ▓▓▓▓▓▓▓▓▓░ 90%
🟢 ATS Scoring           ▓▓▓▓▓▓▓░░░ 70%
⏸️ JD Matching           ░░░░░░░░░░ Paused

🧪 Example API Response
{
  "sections_found": ["experience", "skills", "projects", "education"],
  "skills": [
    "python",
    "machine learning",
    "deep learning",
    "nlp",
    "fastapi",
    "docker",
    "pytorch",
    "tensorflow",
    "sql",
    "java"
  ],
  "resume_score": 71
}

🏗️ Project Structure
backend/
│
├── main.py
├── api/
│   └── analyze.py
│
├── services/
│   ├── parser.py
│   ├── section_detector.py
│   ├── skill_extractor.py
│   ├── scorer.py
│
├── utils/
│   └── file_handler.py
│
└── requirements.txt

🚀 Getting Started
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer/backend

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm

uvicorn main:app --reload


Open 👉 http://127.0.0.1:8000/docs

🧠 How the Resume Is Analyzed (Click)
<details> <summary><b>🔍 Click to expand analysis logic</b></summary>
1. Resume uploaded (PDF / DOCX)
2. Text extracted safely
3. Resume sections detected
4. Skills normalized to canonical form
5. ATS-style scoring applied
6. Structured JSON returned

</details>
🛣️ Engineering Roadmap

 Resume Parsing Engine

 Section Detection

 Skill Normalization

 ATS-Style Scoring

 Resume Feedback Engine

 Frontend Dashboard

 Semantic Job Matching

❌ What This Project Is NOT

❌ Not a keyword-only matcher

❌ Not a frontend-heavy demo

❌ Not an over-engineered ML black box

👨‍💻 Author

Nagraj Rangarej
B.Tech – Artificial Intelligence & Data Science

Backend • NLP • Intelligent Systems

“Build systems that think structurally before thinking statistically.”

⭐ Support

If this project helped or inspired you, consider giving it a ⭐.
