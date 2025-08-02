# 🎓 Personalized Career Guidance System

A full-stack, AI-powered platform designed to guide students and professionals toward the most suitable career paths. It analyzes resumes, evaluates psychometric aptitude, interacts via an intelligent chatbot, and provides tailored job and learning recommendations.

---

## 🗂️ Project Structure

```
career_guidance_system/
├── .env                     # 🔐 Environment variables
├── requirements.txt         # 📦 Python dependencies
├── README.md                # 📘 You're reading it!
│
├── app/                     # 🚀 FastAPI Backend
│   ├── main.py              # 🎯 Entry point of the API
│   ├── routes/              # 📡 All API endpoints
│   ├── models/              # 📄 Data models (Pydantic)
│   ├── ml_models/           # 🤖 Trained ML models
│   ├── utils/               # 🛠️ Utility functions
│   └── data/                # 📊 CSV data files
│
├── frontend/                # 🌐 Streamlit Frontend
│   ├── Home.py              # 🏠 Landing page
│   ├── pages/               # 📑 UI Screens
│   ├── components/          # 🧩 Reusable widgets
│   └── utils/               # 🔁 API integration functions
│
├── resume_samples/          # 📄 Sample resumes for testing
```

---

## 🌟 Key Features

### 📄 Resume Analysis
- Upload your resume in PDF or DOCX format.
- Extracts key skills using NLP techniques.
- Generates job role recommendations using a trained ML model.

### 🧠 Psychometric Test
- 15-question aptitude-based test.
- Scores your responses using a custom scoring model.
- Maps your profile to suitable career domains.

### 📊 Career Recommendations
- Combines resume + test performance + skill set.
- Shows top 5 job roles.
- Uses cosine similarity & clustering to match user profiles with roles.

### 📚 Learning Resources
- Curated learning paths (YouTube, Coursera, etc.).
- Auto-suggested based on extracted skills & job match.
- Personalized upskilling roadmap.

### 💬 Chatbot Assistant
- Smart career mentor powered by NLP (Groke API).
- Asks follow-up questions and suggests next steps.
- Works 24/7 for instant advice.

---

## ⚙️ Technologies Used

### 🧠 Machine Learning & NLP
- `scikit-learn`, `joblib`, `xgboost`, `spaCy`, `transformers`
- Resume vectorization, skill extraction, cosine similarity

### 🚀 Backend - FastAPI
- Modular routes: `/resume/upload`, `/career/recommend`, `/chatbot/respond`, etc.
- Asynchronous, fast, and scalable
- `pydantic` models for validation

### 🌐 Frontend - Streamlit
- Beautiful, interactive UI
- Page-wise navigation (`📄 Resume`, `🧠 Test`, `📊 Results`, `💬 Chatbot`)
- Sidebar for system info, external links, and navigation

---

## 🧪 How to Run Locally

### 🔧 Backend

```bash
cd app/
pip install -r ../requirements.txt
uvicorn main:app --reload
```

### 🌐 Frontend

```bash
cd frontend/
streamlit run Home.py
```

Make sure `.env` file is placed in the root directory with any required keys.

---

## 🧾 Example .env

```
OPENAI_API_KEY=your_openai_key
GROKE_API_KEY=your_groke_key
```

---

## 🧠 Sample Usage

### 1. Upload Resume  
✅ Extracted Skills: `Python`, `Data Analysis`, `Machine Learning`  
🎯 Recommended Jobs: `Data Analyst`, `ML Engineer`

### 2. Take Test  
🧠 Your Psychometric Score: `82%`  
🧭 Strengths: Analytical Thinking, Attention to Detail

### 3. Explore Learning  
📚 Suggested Path:  
- Python for Everybody (Coursera)  
- ML Crash Course (Google)  
- Data Science YouTube Playlist

### 4. Ask the Chatbot  
**You:** _What should I learn next to become a data scientist?_  
**Bot:** _I recommend focusing on statistics, Python libraries like Pandas, and a project portfolio._

---

## 🧑‍💻 Developer Info

### 👨‍🔧 Created by:
**Amal Prasad Trivedi**  
- 🌐 [Portfolio Website](https://amalprasadtrivediportfolio.vercel.app/)  
- 💼 [LinkedIn](https://linkedin.com/in/amal-prasad-trivedi-b47718271/)

---

## 🔗 Project Highlights

| Module        | Tech Used     | Description                              |
|---------------|---------------|------------------------------------------|
| Resume Parser | NLP, PyMuPDF, docx2txt | Extracts skills and keywords       |
| Recommender   | scikit-learn, joblib  | Suggests roles based on user profile |
| Chatbot       | Groke API     | Intelligent conversation system          |
| Test Engine   | Custom Logic  | Maps answers to personality dimensions   |
| UI            | Streamlit     | Clean, intuitive multi-page frontend     |

---

## 📎 License

This project is intended for academic and learning purposes only. All rights reserved to the original developer.

---

> "Empowering careers through AI — one resume at a time!" 🚀
