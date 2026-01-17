📄 Resume Analyzer (React + Flask)

A clean, modern Resume Analyzer web application that evaluates how well a resume matches a selected job role by analyzing skills and generating a Skill Match Score.

This project focuses on clarity, simplicity, and real-world usability, combining a polished frontend with a lightweight backend.

✨ Features

🔍 Resume Skill Analysis
Paste resume content and analyze it against a target job role.

📊 Skill Match Score
Percentage-based score showing how well the resume fits the role.

✅ Matched Skills
Skills found in the resume that align with job requirements.

❌ Missing Skills
Important skills required for the role but not present in the resume.

🎯 Clear Verdict System

❌ Needs Improvement

⚠️ Average Fit

✅ Strong Fit

🌙 Premium Dark UI

Glassmorphism design

Smooth gradients

Modern SaaS-style layout

🧠 How It Works

User pastes resume text

User selects / enters a target role

Backend:

Normalizes text (case, punctuation, formatting)

Matches resume content against predefined role skills

Calculates a match score

Frontend:

Displays score

Shows matched & missing skills as visual cards

Provides a clear verdict

🛠️ Tech Stack
Frontend

React

CSS (Custom Glassmorphism UI)

Backend

Python

Flask

Flask-CORS

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer

2️⃣ Backend Setup (Flask)
cd backend
pip install flask flask-cors
python main.py


Backend runs on:

http://localhost:5000

3️⃣ Frontend Setup (React)
cd frontend
npm install
npm start


Frontend runs on:

http://localhost:3000

🧪 Example Roles Supported

Data Scientist

Web Developer

Software Engineer

Teacher

Actor

(Roles can be easily extended in main.py.)

🎯 Example Output

Skill Match Score: 70%

Matched Skills: Python, Pandas, NumPy

Missing Skills: Statistics, Machine Learning

Verdict: ⚠️ Average Fit

📌 Why This Project?

Clean separation of frontend and backend

Focus on practical skill matching, not buzzwords

Strong UI/UX for demos and interviews

Easy to extend with:

More roles

Advanced NLP

Resume upload (PDF/DOCX)

AI-powered suggestions

🔮 Future Improvements (Optional)

Job description upload

Skill importance weighting

Resume PDF parsing

Role auto-suggestions

AI-based resume improvement tips

👤 Author

Nikhil Rangarej
B.Tech – Artificial Intelligence & Data Science

⭐ Final Note

This project is intentionally simple, readable, and scalable.
It demonstrates both frontend polish and backend logic clarity, making it suitable for learning, demos, and portfolio use.

If you like it, feel free to ⭐ the repository.
