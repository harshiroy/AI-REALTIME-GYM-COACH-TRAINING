# 🏋️ AI Realtime Gym Coach Training

>An AI-powered fitness coaching platform that combines **Computer Vision**, **Pose Estimation**, **Real-Time Exercise Tracking**, **LLM-based Voice Coaching**, and a modern landing page to deliver an interactive workout experience.

---

# 🚀 Live Demo

### 🌐 Landing Page
https://ai-realtime-gym-coach-training.netlify.app/

### 💪 Streamlit Application
https://ai-realtime-gym-coach-training.streamlit.app/

### 📂 GitHub Repository
https://github.com/harshiroy/AI-REALTIME-GYM-COACH-TRAINING

---

# 🧠 Project Overview

AI Realtime Gym Coach Training is a full-stack AI fitness application that uses computer vision and artificial intelligence to analyze workouts in real time.

The system can:

- 🏋 Detect exercises using body pose estimation
- 🔢 Count repetitions automatically
- 📐 Detect incorrect posture
- 🤖 Generate AI coaching feedback
- 🔊 Speak feedback using Text-to-Speech
- 📊 Store workout history
- 🌐 Provide a professional landing website linked with the AI application

---

# ✨ Features

## 🧍 Real-Time Pose Detection

- MediaPipe Pose Landmarker
- 33 body landmarks
- Webcam-based tracking
- Live skeleton visualization

---

## 💪 Supported Exercises

- Squats
- Push-ups
- Lunges
- Shoulder Press
- Biceps Curl

---

## 🔢 Automatic Rep Counter

- Intelligent state-machine logic
- Rep counting
- Set tracking
- Workout completion

---

## 📐 Form Correction

The AI detects common mistakes such as:

- Insufficient squat depth
- Poor posture
- Incorrect elbow position
- Body imbalance
- Fast uncontrolled movement

---

## 🤖 AI Voice Coach

Powered using:

- Groq LLaMA 3
- gTTS

Provides live coaching like:

- "Go deeper."
- "Straighten your back."
- "Control your movement."
- "Excellent rep."

---

## 📊 Workout Tracking

Stores:

- Exercise
- Repetitions
- Sets
- Duration

using SQLite database.

---

# 🏗 Project Architecture

```
AI-REALTIME-GYM-COACH-TRAINING
│
├── LandingPage
│   ├── index.html
│   ├── style.css
│   ├── IMGs
│   ├── videos
│   └── fonts
│
├── Main App
│   ├── core
│   ├── detectors
│   ├── services
│   │   ├── vision
│   │   ├── coaching
│   │   ├── tracking
│   │   ├── persistence
│   │   ├── auth
│   │   └── config
│   │
│   ├── ml_models
│   ├── static
│   ├── main.py
│   └── requirements.txt
│
└── README.md
```

---

# ⚙ Tech Stack

## Programming

- Python

## Computer Vision

- OpenCV
- MediaPipe

## AI

- Groq API (LLaMA 3)

## Voice

- gTTS

## Frontend

- Streamlit
- HTML
- CSS
- JavaScript

## Database

- SQLite

---

# 🔥 Workflow

```
Webcam
    │
    ▼
Pose Detection
(MediaPipe)
    │
    ▼
Joint Angle Calculation
    │
    ▼
Exercise Detection
    │
    ├── Rep Counter
    ├── Form Analysis
    │
    ▼
LLM Coach
(Groq)
    │
    ▼
Voice Feedback
(gTTS)
    │
    ▼
Workout Dashboard
(SQLite)
```

---

# 📷 Demo

## Landing Website

https://ai-realtime-gym-coach-training.netlify.app/

## AI Gym Trainer

https://ai-realtime-gym-coach-training.streamlit.app/

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/harshiroy/AI-REALTIME-GYM-COACH-TRAINING.git
```

Go inside the project

```bash
cd AI-REALTIME-GYM-COACH-TRAINING/Main App
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run main.py
```

---

# 📌 Future Improvements

- Personalized workout plans
- More supported exercises
- Mobile application
- Cloud database
- AI nutrition assistant
- Workout recommendations
- Performance analytics dashboard

---

# 👩‍💻 Developed By

**Harshita Roy**

Artificial Intelligence & Data Science Student

---

## 🔗 Links

### GitHub

https://github.com/harshiroy/AI-REALTIME-GYM-COACH-TRAINING

### Landing Website

https://ai-realtime-gym-coach-training.netlify.app/

### Live Application

https://ai-realtime-gym-coach-training.streamlit.app/

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

It really helps and motivates future development.

---

# 📜 License

This project is intended for educational and research purposes.
