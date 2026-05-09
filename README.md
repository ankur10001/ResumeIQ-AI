# 🧠 HireSense AI

> **AI-Powered Resume & Interview Intelligence Platform**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-red?logo=streamlit)](https://streamlit.io)
[![Gemini API](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange?logo=google)](https://ai.google.dev)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🚀 Overview

**HireSense AI** is an LLM-powered resume intelligence platform that leverages **Google Gemini 2.5 Flash** and advanced **prompt engineering** to give job seekers a competitive edge in the hiring process.

Upload your resume PDF, paste a job description, and within seconds get:
- An AI-generated **ATS compatibility score** with dimensional breakdown
- **Skills gap analysis** powered by semantic NLP techniques
- An **AI Interview Copilot** with role-specific questions
- A personalized **90-day career roadmap**

### Architecture

```
PDF Upload → Text Extraction → Prompt Engineering → Gemini API → Structured JSON → UI Rendering
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 **ATS Score Engine** | AI-driven ATS compatibility score (0–100) with skills, keyword, experience & formatting sub-scores |
| 🔍 **Skills Gap Analysis** | NLP-based detection of missing technical skills, tools, and ATS keywords |
| 🎤 **Interview Copilot** | Generates HR, technical, project, and behavioral interview questions from your resume + JD |
| 🗺️ **90-Day Career Roadmap** | Personalized week-by-week action plan to bridge skill gaps |
| 💡 **Improvement Suggestions** | Actionable recommendations and certification suggestions |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.9+** | Core language |
| **Streamlit** | Interactive web UI framework |
| **Google Gemini 2.5 Flash** | LLM for AI-driven analysis & prompt engineering |
| **PyPDF2** | PDF text extraction |
| **python-dotenv** | Secure API key management |

---

## 📁 Project Structure

```
hiresense-ai/
│
├── app.py              # Main Streamlit application entry point
├── utils.py            # Helper functions: PDF extraction, Gemini API calls, UI rendering
├── prompts.py          # Centralized prompt engineering templates
├── requirements.txt    # Python dependencies
├── .env                # API keys (NOT committed to git)
├── .env.example        # Template for environment variables
└── README.md           # Project documentation
```

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- A [Google Gemini API key](https://ai.google.dev/) (free tier available)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/hiresense-ai.git
cd hiresense-ai
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` and add your API key:
```env
GOOGLE_API_KEY=your_actual_gemini_api_key_here
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 📖 Usage

1. **Upload Resume** — Drag & drop your resume PDF in the sidebar
2. **Paste Job Description** — Copy the full job posting into the text area
3. **Click "Analyze with AI"** — The pipeline runs 4 sequential Gemini API calls
4. **Explore Results** — Navigate through the 4 result tabs:
   - `📊 ATS Score Analysis` — Compatibility scores with visual metrics
   - `🔍 Skills Gap Analysis` — Missing skills and improvement suggestions
   - `🎤 Interview Copilot` — 16 role-specific interview questions with tips
   - `🗺️ Career Roadmap` — 90-day action plan to land the job

---

## 📸 Screenshots

> *Add screenshots here after running the application*

| Dashboard | ATS Score | Interview Copilot |
|---|---|---|
| ![Dashboard](screenshots/dashboard.png) | ![ATS Score](screenshots/ats_score.png) | ![Interview](screenshots/interview.png) |

---

## 🧠 Technical Highlights

- **Prompt Engineering**: Each of the 4 analysis modules uses a carefully engineered prompt that instructs the LLM to return structured JSON, enabling reliable parsing and rich UI rendering.
- **Semantic NLP Analysis**: Gemini performs deep semantic comparison between resume content and JD, going beyond simple keyword matching.
- **ATS Optimization Engine**: Multi-dimensional scoring across skills alignment, keyword density, experience relevance, and formatting quality.
- **Modular Architecture**: Clean separation of concerns — prompts, utilities, and UI logic are fully decoupled.

---

## 🚀 Deployment on Streamlit Cloud

1. Push your project to a **GitHub repository**
2. Visit [share.streamlit.io](https://share.streamlit.io) and connect your GitHub
3. Select `app.py` as the entry point
4. Add your `GOOGLE_API_KEY` in **Streamlit Secrets** (Settings → Secrets):
   ```toml
   GOOGLE_API_KEY = "your_api_key_here"
   ```
5. Deploy — your app will be live at `https://yourapp.streamlit.app`

> **Note**: Update the `.env` loading in `app.py` to also read from `st.secrets` for cloud compatibility.

---

## 🔮 Future Improvements

- [ ] **Multi-format support** — DOCX, TXT resume uploads
- [ ] **Resume rewriting** — AI-powered resume bullet point optimizer
- [ ] **Cover letter generator** — Auto-generate tailored cover letters
- [ ] **Job board integration** — Scrape job descriptions from LinkedIn/Indeed URLs
- [ ] **Interview simulator** — Real-time mock interview with audio transcription
- [ ] **Resume PDF export** — Download an optimized version of the resume

---

## 📄 License

MIT License — feel free to fork, modify, and use for personal or commercial projects.

---

## 🙋‍♂️ About

Built as a portfolio project demonstrating:
- LLM integration and prompt engineering with Google Gemini API
- Full-stack Python AI application development
- ATS optimization and NLP-driven resume analysis
- Professional Streamlit UI/UX design patterns
