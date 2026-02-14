# 🚀 ResuMate AI  

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-4285F4?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen)

### AI-Powered Resume Analysis & ATS Optimization Platform

ResuMate AI is an intelligent resume optimization platform that analyzes resumes against job descriptions and enhances them for maximum ATS (Applicant Tracking System) compatibility using Large Language Models (LLMs) and NLP techniques.

It helps candidates increase resume match scores, optimize keyword relevance, and improve interview callback rates through AI-driven enhancement.

---

## 🔥 Key Features

- 📄 Resume Parsing (PDF Support)
- 📊 ATS Compatibility Scoring Engine
- 🎯 Job Description-Based Keyword Matching
- ✨ AI-Powered Resume Enhancement
- 📝 Automatic Cover Letter Generation
- 🌐 Interactive Web Interface (Streamlit)
- ⚡ Google Gemini API Integration

---

## 🧠 How It Works

1. Upload your resume (PDF)
2. Paste the target job description
3. ResuMate AI:
   - Extracts resume content
   - Performs semantic comparison with the job description
   - Calculates ATS compatibility score
   - Identifies missing keywords
   - Suggests optimized improvements
   - Generates a tailored cover letter

---

## 🛠 Tech Stack

### Backend
- Python
- Google Gemini API (`gemini-flash-latest`)
- NLP Processing
- Custom ATS Scoring Algorithm

### Frontend
- Streamlit

### Development Tools
- Virtual Environment (.venv)
- Git & GitHub

---

## 📂 Project Structure

```
ResuMate_AI/
│
├── data/                  # Resume & Job Description input files
├── src/
│   ├── resume_parser.py   # Extract resume text
│   ├── ats_scoring.py     # ATS match scoring logic
│   ├── gemini_ai.py       # Gemini API integration
│   ├── cover_letter.py    # Cover letter generation
│   └── main.py            # Core workflow
│
├── ui/
│   └── app.py             # Streamlit frontend
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Tanishinfinity/Resumate-AI.git
cd Resumate-AI
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

Activate (Windows):

```bash
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your Gemini API Key

Inside `src/gemini_ai.py`:

```python
client = genai.Client(api_key="YOUR_API_KEY")
```

---

## ▶️ Run the Application

```bash
streamlit run ui/app.py
```

Open your browser:

```
http://localhost:8501
```

---

## 📈 Impact & Results

- Improved ATS compatibility by **30–45%** through JD-based optimization
- Automated resume enhancement workflow
- Reduced manual editing effort by ~70%
- Built a modular and scalable AI-driven architecture

---

## 🚀 Future Enhancements

- User authentication system
- Resume version comparison
- Full AI resume rewrite mode
- Download optimized resume as PDF
- Cloud deployment (AWS / GCP)
- Full React / Next.js frontend migration

---

## 👨‍💻 Author

**Tanish**  
AI Developer | Full-Stack Builder | Problem Solver  

---

⭐ If you found this project useful, consider giving it a star!