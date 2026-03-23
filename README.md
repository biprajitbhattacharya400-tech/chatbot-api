# 🚀 FastAPI + Groq LLM + Semantic RAG + AI Agent

A **production-style AI backend** built with **FastAPI**, integrating **Groq LLM**, **Semantic RAG (Retrieval-Augmented Generation)**, and an intelligent **tool-using AI Agent (LangChain)**.

This project demonstrates how modern AI systems combine:

* ⚡ High-performance backend APIs
* 🧠 Large Language Models (LLMs)
* 🔍 Semantic search with embeddings
* 🔗 Retrieval-Augmented Generation (RAG)
* 🤖 Autonomous agents with tool usage

---

## 🌟 Key Highlights

* ⚡ FastAPI-based scalable backend
* 🧠 Groq-powered LLM (LLaMA 3.3 70B)
* 🔥 Semantic RAG pipeline using embeddings
* 🤖 AI Agent that **chooses tools automatically**
* 🧮 Built-in Calculator Tool
* 📄 Document Search Tool (vector similarity)
* 🗄️ SQLAlchemy + SQLite integration
* 📦 Clean, modular, production-ready structure

---

## 🛠️ Tech Stack

| Category      | Technology            |
| ------------- | --------------------- |
| Backend       | FastAPI               |
| Database      | SQLite + SQLAlchemy   |
| LLM           | Groq (LLaMA 3.3 70B)  |
| Embeddings    | Sentence Transformers |
| AI Framework  | LangChain             |
| Environment   | Python-dotenv         |
| Numerical Ops | NumPy                 |

---

## 📂 Project Structure

```
.
├── main.py
├── users.db
├── requirements.txt
├── .env              # (not committed)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/biprajitbhattacharya400-tech/chatbot-api.git
cd chatbot-api
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Linux/Mac
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the Server

```bash
python -m uvicorn main:app --reload
```

---

### 6️⃣ Open API Docs

👉 http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

### 🏠 Root

```
GET /
```

---

### 👤 User Management

```
GET    /users
GET    /users/top
POST   /users/
```

---

### 🤖 LLM Endpoint

```
POST /ask-ai
```

Direct interaction with Groq LLM.

---

### 🔥 RAG Endpoint

```
POST /ask-doc
```

* Converts query → embedding
* Finds relevant documents
* Passes context → LLM

---

### ⚡ AI Agent Endpoint

```
POST /agent
```

An intelligent agent that:

* Chooses tools dynamically
* Performs reasoning
* Executes actions

---

## 🧠 System Architecture

### 🔹 Basic LLM Flow

```
User → LLM → Response
```

---

### 🔹 RAG Flow

```
User Query
   ↓
Embedding
   ↓
Vector Similarity Search
   ↓
Top Documents Retrieved
   ↓
LLM Generates Answer
```

---

### 🔹 AI Agent Flow

```
User Query
   ↓
LLM Agent
   ↓
Decision Making:
   → Calculator Tool
   → Document Search Tool
   ↓
Tool Execution
   ↓
Final Answer
```

---

## 🔧 Tools Used by Agent

### 🧮 Calculator Tool

* Handles mathematical expressions safely

### 📄 Document Search Tool

* Uses embedding similarity
* Retrieves top relevant documents

---

## 🧪 Example Queries

### ➤ Calculator

```
What is 25 * 4?
```

### ➤ RAG

```
What is Retrieval-Augmented Generation?
```

### ➤ Agent

```
Explain FastAPI
What is 15 + 27?
```

---

## 🆚 Keyword vs Semantic Search

| Approach        | Limitation           | Result   |
| --------------- | -------------------- | -------- |
| Keyword Search  | Exact match required | ❌ Poor   |
| Semantic Search | Understands meaning  | ✅ Better |

---

## ⚠️ Common Issues

* ❌ Missing API key → Check `.env`
* ❌ First run slow → Model download
* ❌ Import errors → Reinstall dependencies
* ❌ Env mismatch → Activate `.venv`

---

## 🚀 Future Improvements

* 🔥 Vector DB (FAISS / Pinecone)
* 📂 File upload (PDF, TXT)
* 💬 Chat memory (multi-turn)
* ⚡ Streaming responses
* 🌐 Frontend (React / Next.js)
* ☁️ Deployment (Render / Railway)

---

## 🙌 What This Project Demonstrates

* Backend API engineering
* LLM integration in production systems
* Semantic search & embeddings
* Retrieval-Augmented Generation (RAG)
* Tool-using AI agents

---

## 📜 License

Open-source and free to use.

---

## ⭐ Support

If you found this useful:

👉 Star the repo
👉 Share it
👉 Build on top of it

---

💡 Built with curiosity, learning, and real-world AI engineering principles.
