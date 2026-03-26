# 🚀 AI Chatbot API (FastAPI + RAG + LangChain + Groq)

A production-ready AI backend built with **FastAPI**, featuring:

- 🔍 Retrieval-Augmented Generation (RAG)
- 🤖 LangChain Agent with tools
- ⚡ Groq LLM integration
- 🧠 Semantic search using Sentence Transformers
- 🗄️ SQLAlchemy database
- 🌐 Deployed live on Render

---

## 🌐 Live Demo

👉 https://chatbot-api-jrrh.onrender.com/docs

---

## 🧠 Features

### ✅ AI Capabilities
- Chat with LLM using Groq API
- Document-based Q&A (RAG)
- Intelligent agent with tools:
  - Calculator 🧮
  - Document Search 📄

### ✅ Backend
- FastAPI REST API
- SQLAlchemy ORM
- SQLite database (default)
- Environment-based config

### ✅ Production Ready
- Lazy loading for heavy models
- Cached embeddings using `lru_cache`
- Optimized for cloud deployment (Render)

---

## 🏗️ Tech Stack

- FastAPI
- LangChain
- Groq API
- Sentence Transformers
- SQLAlchemy
- NumPy
- Python-dotenv

---

## 📁 Project Structure

```text
chatbot-api/
│
├── main.py            # Main FastAPI app
├── requirements.txt   # Dependencies
├── runtime.txt        # Python version (3.11)
├── users.db           # SQLite DB
├── README.md
```

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone Repo
```bash
git clone https://github.com/your-username/chatbot-api.git
cd chatbot-api
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Run Server
```bash
uvicorn main:app --reload
```

👉 Open: http://127.0.0.1:8000/docs

---

## 🚀 Deployment (Render)

### 1️⃣ Required Files
- `requirements.txt`
- `runtime.txt` → `python-3.11`

### 2️⃣ Environment Variables (Render Dashboard)

| Key | Value |
|-----|-------|
| GROQ_API_KEY | your_key |
| ENV | production |

### 3️⃣ Start Command
```bash
uvicorn main:app --host 0.0.0.0 --port /$PORT
```

### 4️⃣ Deploy Steps
- Push code to GitHub
- Connect repo to Render
- Click Deploy 🚀

---

## ⚡ Key Optimization (IMPORTANT)

### Lazy Loading + Caching

Heavy models are **not loaded at startup**:

```python
from functools import lru_cache

@lru_cache(maxsize=1)
def get_embedding_model():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer("all-MiniLM-L6-v2")
```

### Why?
- Faster startup
- Prevents crashes on deployment
- Reduces memory usage

---

## 🧪 API Endpoints

### 🏠 Health
- `GET /`
- `GET /health`

### 👤 Users
- `GET /users`
- `GET /users/top`
- `POST /users`

### 🤖 AI Chat
- `POST /ask-ai`

Example:
```json
{
  "prompt": "Explain FastAPI"
}
```

### 📄 RAG
- `POST /ask-doc`

### 🧠 Agent
- `POST /agent`

---

## 🔥 Real Deployment Challenges

### ❌ Module Errors
- `ModuleNotFoundError: No module named 'dotenv'`

### ❌ Dependency Conflicts
- LangChain version mismatch

### ❌ Runtime Crash
- Heavy models loading at startup
- App failed before port binding

### ❌ Render Error
- No open ports detected

---

## ✅ Solutions Applied

- Fixed dependency versions
- Added missing packages (`python-dotenv`)
- Forced Python 3.11
- Used environment variables correctly
- Implemented lazy loading + caching

---

## 📈 Future Improvements

- Frontend (React / Next.js)
- Streaming responses
- Vector DB (FAISS / Pinecone)
- Authentication
- Docker support

---

## 🤝 Contributing

Feel free to fork and improve the project!

---

## 📜 License

MIT License

---

## 💬 Author

Built with ❤️ by Biprajit

---

## ⭐ Support

If you found this useful:

- Star ⭐ the repo
- Share it
- Build on top of it 🚀