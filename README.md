🚀 Resume Analyzer – Intelligent Resume Parsing & Scoring System
<p align="center"> <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=36BCF7&center=true&vCenter=true&width=800&lines=FastAPI+%7C+NLP+%7C+ATS-Style+Resume+Analysis;PDF+%26+DOCX+Resume+Parsing;Skill+Extraction+%26+Resume+Scoring;Built+for+Scalability+and+Future+AI+Extensions" /> </p> <p align="center"> <b>An intelligent backend system that parses resumes, extracts structured insights, and generates ATS-style resume scores using NLP.</b> </p>
🧠 Project Overview

Resume Analyzer is a backend-driven NLP system designed to analyze resumes the way real Applicant Tracking Systems (ATS) do.

Unlike simple keyword matchers, this project focuses on:

Resume structure

Skill normalization

Section depth

Scoring realism

The architecture is intentionally built to support future AI/ML enhancements such as semantic job matching and feedback intelligence.

✨ Live System Flow (Animated)
Resume Upload → Text Extraction → Section Detection
              → Skill Extraction → Resume Scoring
              → Structured JSON Output

<p align="center"> <img src="https://user-images.githubusercontent.com/placeholder/resume-analyzer-flow.gif" width="80%" /> </p>

<details>
  <summary><b>🔍 Click to See Resume Analysis Logic</b></summary>

### Step-by-Step Logic
1. Resume uploaded (PDF/DOCX)
2. Text extracted
3. Sections detected
4. Skills normalized
5. ATS-style score generated

</details>

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

Handles variations like:

ML → Machine Learning

DL → Deep Learning

Avoids duplicate & noisy skills

📊 ATS-Style Resume Scoring

Scores resumes on a 0–100 scale

Considers:

Section presence

Section depth

Skill diversity

Prevents score inflation

⚡ FastAPI Backend

Modular service-based architecture

Swagger UI for instant testing

Scalable & production-ready

📸 API Demo (Live Testing)
<p align="center"> <img src="https://user-images.githubusercontent.com/placeholder/swagger-demo.gif" width="85%" /> </p>

🧠 Example API Response
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

⚙️ Tech Stack

| Layer         | Technology              |
| ------------- | ----------------------- |
| Backend       | FastAPI                 |
| NLP           | spaCy                   |
| ML (Optional) | Sentence Transformers   |
| Parsing       | pdfplumber, python-docx |
| Language      | Python 3.10+            |

🚀 Getting Started
1️⃣ Clone Repository
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer/backend

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

4️⃣ Run Server
uvicorn main:app --reload

5️⃣ Test API

Open 👉 http://127.0.0.1:8000/docs

🧪 Tested Scenarios

Student resumes

Technical resumes

NLP-heavy profiles

Backend developer profiles

🛑 What This Project Is NOT

❌ Not a keyword-only matcher

❌ Not a frontend-heavy demo

❌ Not over-engineered with unnecessary transformers

🔮 Future Enhancements (Planned)

Resume ↔ Job Description semantic matching

Resume improvement feedback engine

Frontend dashboard (React)

Role-based scoring (ML Engineer, Backend Dev, etc.)

Exportable reports (PDF)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Status](https://img.shields.io/badge/Status-Phase%201%20Complete-success)
![License](https://img.shields.io/badge/License-MIT-yellow)



👨‍💻 Author

Nagraj Rangarej
B.Tech – Artificial Intelligence & Data Science
Backend | NLP | Intelligent Systems

“Build systems that think structurally before thinking statistically.”

⭐ If You Like This Project

Give it a ⭐ — it helps visibility and motivates further development.
