🚀 Resume Analyzer — Intelligent ATS-Style Resume Scoring System
<p align="center"> <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=900&color=36BCF7&center=true&vCenter=true&width=900&lines=FastAPI+%7C+NLP+Backend+System;ATS-Style+Resume+Parsing+and+Scoring;PDF+%26+DOCX+Resume+Analysis;Built+for+Scalability+and+Future+AI+Extensions" /> </p> <p align="center"> <b>An intelligent backend system that parses resumes, extracts structured insights, and generates ATS-style resume scores using NLP.</b> </p>
---------------------------------------------------------------------------------------

🧠 Project Overview

* Resume Analyzer is a backend-driven NLP system designed to analyze resumes the way real Applicant Tracking Systems (ATS) do.

* Unlike simple keyword matchers, this system focuses on:

Resume structure

Skill normalization

Section depth

Realistic scoring, not inflated results

The architecture is intentionally designed to support future AI/ML enhancements such as semantic job matching and automated resume feedback.

---------------------------------------------------------------------------------------
🔥 Key Features

📄 Resume Parsing

Supports PDF and DOCX

Clean text extraction

Handles real-world resume formatting

---------------------------------------------------------------------------------------

🧩 Section Detection

Automatically identifies:

Experience

Skills

Projects

Education

---------------------------------------------------------------------------------------

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

---------------------------------------------------------------------------------------

⚙️ Tech Stack

| Layer         | Technology              |
| ------------- | ----------------------- |
| Backend       | FastAPI                 |
| NLP           | spaCy                   |
| ML (Optional) | Sentence Transformers   |
| Parsing       | pdfplumber, python-docx |
| Language      | Python 3.10+            |

---------------------------------------------------------------------------------------

## ⚙️ System Status

- Resume Parsing: ✅ Complete
- Section Detection: ✅ Complete
- Skill Normalization: ✅ Complete
- ATS-Style Scoring: ✅ Complete
- Job Description Matching: ⏸️ Paused

---------------------------------------------------------------------------------------

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Status](https://img.shields.io/badge/Status-Phase%201%20Complete-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---------------------------------------------------------------------------------------
```bash
🚀 Getting Started
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer/backend

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm

uvicorn main:app --reload

Open 👉 http://127.0.0.1:8000/docs
```

---------------------------------------------------------------------------------------

🛣️ Engineering Roadmap

 Resume Parsing Engine

 Section Detection

 Skill Normalization

 ATS-Style Scoring

 Resume Feedback Engine

 Frontend Dashboard

 Semantic Job Matching

---------------------------------------------------------------------------------------

 👨‍💻 Author

Nagraj Rangarej
B.Tech – Artificial Intelligence & Data Science

Backend • NLP • Intelligent Systems

---------------------------------------------------------------------------------------

```text
“Build systems that think structurally before thinking statistically.”
```

---------------------------------------------------------------------------------------

⭐ Support

If this project helped or inspired you, consider giving it a ⭐.
