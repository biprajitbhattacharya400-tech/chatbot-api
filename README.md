# 🚀 FastAPI + Groq LLM + Semantic RAG + AI Agent

A production-style backend project built with **FastAPI**, integrating **Groq LLM**, **Semantic RAG (vector embeddings)**, and an **AI Agent using LangChain**.

This system demonstrates how modern AI applications combine:
- Backend APIs
- Retrieval-Augmented Generation (RAG)
- Vector search
- Tool-using AI agents

---

## 📌 Features

* 🧱 REST API using FastAPI  
* 🗄️ SQLite database with SQLAlchemy  
* 👤 User management system  
* 🤖 LLM-powered endpoint (`/ask-ai`)  
* 🔥 Semantic RAG system (`/ask-doc`)  
* 🧠 Vector-based document retrieval (embeddings)  
* ⚡ AI Agent with tool usage (`/agent`)  
* 🔧 Multi-tool system (Calculator + Document Search)  

---

## 🛠️ Tech Stack

* FastAPI  
* SQLAlchemy  
* SQLite  
* Pydantic  
* Groq API (LLaMA 3.3 70B)  
* Sentence-Transformers  
* NumPy  
* LangChain  
* Python-dotenv  

---

## 📂 Project Structure

```
.
├── main.py
├── users.db
├── .env
├── requirements.txt
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

Or manually:

```bash
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv groq
pip install sentence-transformers torch numpy
pip install langchain langchain-community langchain-core langchain-groq
```

---

### 4️⃣ Set up environment variables

Create `.env` file:

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

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### 🏠 Root
```
GET /
```

---

### 👤 User APIs
```
GET /users
GET /users/top
POST /users/
```

---

### 🤖 Ask AI (LLM)
```
POST /ask-ai
```

---

### 🔥 Ask AI with RAG
```
POST /ask-doc
```

Uses semantic search to retrieve relevant documents before generating answers.

---

### ⚡ AI Agent (LangChain)
```
POST /agent
```

This endpoint uses an **AI Agent** that can:
- Perform calculations
- Search documents
- Decide which tool to use automatically

---

## 🧠 How It Works

### 🔹 Basic LLM
```
User → LLM → Response
```

---

### 🔹 Semantic RAG
```
User → Convert to Embedding → Compare with Documents → Retrieve → LLM → Answer
```

---

### 🔹 AI Agent (LangChain)

```
User Query
   ↓
Agent (LLM)
   ↓
Decides:
   → Calculator Tool
   → Document Search Tool
   ↓
Executes tool
   ↓
Returns final answer
```

---

## 🔧 Tools Used by Agent

### 🧮 Calculator Tool
Handles mathematical queries using Python evaluation.

### 📄 Document Search Tool
Uses embedding-based similarity search for retrieving relevant context.

---

## 🧠 Example Queries

### Calculator:
```
What is 25 * 4?
```

### RAG:
```
What is RAG?
```

### Agent:
```
Explain RAG
What is 10 + 15?
```

---

## 🆚 Keyword vs Semantic Search

| Approach            | Limitation          | Improvement |
|---------------------|---------------------|-------------|
| Keyword Matching    | Needs exact words   |     ❌      |
| Embeddings          | Understands meaning |     ✅      |

---

## ⚠️ Common Issues

* ❌ Missing API key → check `.env`  
* ❌ First run slow → model download  
* ❌ Import errors → install all dependencies  

---

## 💡 Future Improvements

* 🔥 Vector database (FAISS / Pinecone)  
* 📂 Upload documents (PDF, TXT)  
* 💬 Chat memory (multi-turn agents)  
* ⚡ Streaming responses  
* 🌐 Frontend integration  

---

## 🙌 Acknowledgements

Built to explore:

* Backend API development  
* LLM integration  
* Semantic search  
* Retrieval-Augmented Generation (RAG)  
* AI Agents (LangChain)  

---

## 📜 License

Open-source and free to use.

---

⭐ If you found this helpful, consider giving it a star!