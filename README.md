# 🚀 FastAPI + Groq LLM + RAG API Project

A clean and simple backend project built with **FastAPI**, **SQLAlchemy**, and **Groq LLM integration**.

This API allows you to manage users, interact with an AI model, and now includes a **Retrieval-Augmented Generation (RAG)** system for more accurate, context-aware responses.

---

## 📌 Features

* 🧱 REST API using FastAPI
* 🗄️ SQLite database with SQLAlchemy
* 👤 User management (CRUD basics)
* 🤖 AI-powered endpoint using Groq (LLaMA 3.3 model)
* 🔐 Environment variable support for API keys
* 🔥 Retrieval-Augmented Generation (RAG) system (`/ask-doc`)
* 📄 Context-based AI responses using custom documents

---

## 🛠️ Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Groq API (LLM - LLaMA 3.3 70B)
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
git clone https://github.com/biprajitbhattacharya400-tech/chatbot-api.git
cd chatbot-api
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
pip install -r requirements.txt
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

### 🤖 Ask AI (General LLM)

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

### 🔥 Ask AI with Documents (RAG)

```
POST /ask-doc
```

**Request Body:**

```json
{
  "prompt": "What is RAG?"
}
```

**Response:**

```json
{
  "answer": "RAG stands for Retrieval Augmented Generation...",
  "context_used": [
    "RAG stands for Retrieval Augmented Generation..."
  ]
}
```

---

## 🧠 How AI Integration Works

### 🤖 Basic LLM (`/ask-ai`)

1. User sends a prompt  
2. FastAPI receives it via Pydantic model  
3. Prompt is sent to Groq LLM  
4. Model generates response  
5. API returns the answer  

---

### 🔥 RAG System (`/ask-doc`)

1. User sends a question  
2. System searches relevant documents using keyword matching (`search_docs`)  
3. Top matching documents are selected  
4. Documents are passed as **context** to the LLM  
5. LLM generates answer based only on that context  

👉 This improves:
- Accuracy  
- Reliability  
- Reduces hallucination  

---

## 🧠 Example RAG Flow

```
User Question → Search Docs → Add Context → LLM → Answer
```

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
* 📂 Upload custom documents (PDF, TXT)
* 🧠 Vector database (FAISS / Pinecone for advanced RAG)

---

## 🙌 Acknowledgements

Built as a learning + practical project to understand:

* Backend APIs  
* Database integration  
* LLM integration in real-world apps  
* Retrieval-Augmented Generation (RAG)  

---

## 📜 License

This project is open-source and free to use.

---

⭐ If you found this helpful, consider giving it a star!