# ⚽ Smart Foot Comment – AI Football Commentary System

**Smart Foot Comment** is an intelligent football commentary system that uses Artificial Intelligence to generate natural and dynamic football match commentary in Arabic and French.

The project aims to transform football match events into professional-style commentary, with the goal of developing a real-time AI commentary experience.

## 🚀 Features

- 🤖 AI-powered football commentary using Groq API.
- 🌍 Multilingual support: Arabic and French.
- ⚽ Football match management.
- 📋 Match event management.
- 🗄️ SQLite database integration.
- 🔌 REST API built with FastAPI.
- 📝 Automatic commentary generation based on match events.

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | Backend REST API |
| SQLite | Database |
| Groq API | AI commentary generation |
| Pydantic | Data validation |
| Uvicorn | ASGI server |

## 📁 Project Structure

```text
Smart_Foot_Comment/
│
├── ai_engine/
│   ├── commentary/
│   │   ├── prompt_manager.py
│   │   ├── llm_client.py
│   │   └── commentary_engine.py
│   │
│   └── event_detection/
│       ├── event_classifier.py
│       └── event_fusion.py
│
├── backend/
│   └── app/
│       ├── main.py
│       ├── schemas/
│       ├── database/
│       └── services/
│
├── requirements/
├── Rapport/
├── .env.example
├── .gitignore
├── README.md
└── run.py
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart_Foot_Comment.git
cd Smart_Foot_Comment
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements/requirements.txt
```

### 5. Configure the API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Never publish your API key.

### 6. Run the backend

```bash
python -m uvicorn backend.app.main:app --reload
```

## 🌐 API Documentation

After starting the server, open:

http://127.0.0.1:8000/docs

### Main endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API home |
| GET | `/health` | Health check |
| POST | `/matches` | Create a match |
| GET | `/matches` | Get all matches |
| GET | `/matches/{match_id}` | Get match details |
| POST | `/matches/{match_id}/events` | Add a match event |
| GET | `/matches/{match_id}/events` | Get match events |
| POST | `/matches/{match_id}/commentary` | Generate AI commentary |

## 💬 Commentary Languages

The system currently supports:

- Arabic (`ar`)
- French (`fr`)

## 🗺️ Future Improvements

- Real-time football event detection.
- Live commentary using WebSockets.
- Computer vision integration with OpenCV and YOLO.
- Football match data API integration.
- Text-to-Speech commentary.
- React frontend dashboard.

## 👨‍💻 Author

Developed as an AI and football technology project.

**Smart Foot Comment – Bringing Football Matches to Life with AI!**