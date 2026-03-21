# 🚀 FastAPI + Groq LLM API Project

A clean and simple backend project built with **FastAPI**, **SQLAlchemy**, and **Groq LLM integration**.
This API allows you to manage users and interact with an AI model through a dedicated endpoint.

---

## 📌 Features

* 🧱 REST API using FastAPI
* 🗄️ SQLite database with SQLAlchemy
* 👤 User management (CRUD basics)
* 🤖 AI-powered endpoint using Groq (LLaMA 3.3 model)
* 🔐 Environment variable support for API keys

---

## 🛠️ Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Groq API (LLM)
* Python-dotenv

---

## 📂 Project Structure

```
.
├── main.py          # Main FastAPI application
├── users.db         # SQLite database (auto-created)
├── .env             # Environment variables (API key)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv groq
```

---

### 4️⃣ Set up environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the server

```bash
uvicorn main:app --reload
```

---

### 6️⃣ Open API docs

Visit:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### 🏠 Root

```
GET /
```

Returns API status.

---

### 👤 Get all users

```
GET /users
```

---

### 🏆 Get top users (score > 80)

```
GET /users/top
```

---

### ➕ Create user

```
POST /users/
```

**Request Body:**

```json
{
  "name": "John",
  "score": 90
}
```

---

### 🤖 Ask AI

```
POST /ask-ai
```

**Request Body:**

```json
{
  "prompt": "What is FastAPI?"
}
```

**Response:**

```json
{
  "response": "FastAPI is a modern Python web framework..."
}
```

---

## 🧠 How AI Integration Works

1. User sends a prompt
2. FastAPI receives it via Pydantic model
3. Prompt is sent to Groq LLM
4. Model generates response
5. API returns the answer

---

## ⚠️ Common Issues

* ❌ API key not set → ensure `.env` is loaded
* ❌ Wrong method name → use `completions.create()`
* ❌ Typo in response → use `message.content`

---

## 💡 Future Improvements

* Chat history (multi-turn conversation)
* Streaming responses
* Authentication system
* Frontend integration (React / Next.js)

---

## 🙌 Acknowledgements

Built as a learning + practical project to understand:

* Backend APIs
* Database integration
* LLM integration in real-world apps

---

## 📜 License

This project is open-source and free to use.

---

⭐ If you found this helpful, consider giving it a star!
