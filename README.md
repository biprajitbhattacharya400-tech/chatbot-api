# 🚀 FastAPI + Groq LLM + Semantic RAG API Project

A clean and scalable backend project built with **FastAPI**, **SQLAlchemy**, and **Groq LLM integration**.

This API combines traditional backend development with modern AI capabilities, including a **Retrieval-Augmented Generation (RAG)** system powered by **vector embeddings** for semantic search.

---

## 📌 Features

* 🧱 REST API using FastAPI  
* 🗄️ SQLite database with SQLAlchemy  
* 👤 User management (CRUD basics)  
* 🤖 AI-powered endpoint using Groq (LLaMA 3.3 model)  
* 🔐 Environment variable support for API keys  
* 🔥 Semantic RAG system (`/ask-doc`)  
* 🧠 Vector-based document retrieval using embeddings  
* 📄 Context-aware AI responses  

---

## 🛠️ Tech Stack

* FastAPI  
* SQLAlchemy  
* SQLite  
* Pydantic  
* Groq API (LLaMA 3.3 70B)  
* Sentence-Transformers  
* NumPy  
* Python-dotenv  

---

## 📂 Project Structure

```
.
├── main.py          # Main FastAPI application
├── users.db         # SQLite database (auto-created)
├── .env             # Environment variables (API key)
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

---

### 4️⃣ Set up environment variables

Create a `.env` file:

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

### 👤 Get all users

```
GET /users
```

---

### 🏆 Get top users

```
GET /users/top
```

---

### ➕ Create user

```
POST /users/
```

---

### 🤖 Ask AI (General LLM)

```
POST /ask-ai
```

---

### 🔥 Ask AI with Semantic RAG

```
POST /ask-doc
```

**Request Body:**

```json
{
  "prompt": "Explain RAG"
}
```

**Response:**

```json
{
  "answer": "...",
  "context_used": ["..."]
}
```

---

## 🧠 How AI Integration Works

### 🤖 Basic LLM (`/ask-ai`)

1. User sends prompt  
2. Sent directly to LLM  
3. Response returned  

---

### 🔥 Semantic RAG System (`/ask-doc`)

1. Documents are converted into **vector embeddings**  
2. User query is also converted into an embedding  
3. Cosine similarity is used to find the most relevant documents  
4. Top documents are passed as **context** to the LLM  
5. LLM generates answer based on that context  

---

## 🧠 Example Flow

```
User Query → Convert to Vector → Compare with Doc Vectors → Retrieve Top Docs → LLM → Answer
```

---

## 🆚 Keyword Search vs Semantic Search

| Approach          | Limitation          | Improvement |
|-------------------|---------------------|-------------|
| Keyword Matching  | Needs exact words   |     ❌      |
| Vector Embeddings | Understands meaning |     ✅      |

Example:

```
"Explain RAG" ≈ "What is Retrieval Augmented Generation"
```

---

## ⚠️ Common Issues

* ❌ Missing API key → check `.env`  
* ❌ Model download delay → first run takes time  
* ❌ Missing dependencies → install `sentence-transformers`, `torch`, `numpy`  

---

## 💡 Future Improvements

* ⚡ Vector database (FAISS / Pinecone)  
* 📂 Upload custom documents (PDF, TXT)  
* 💬 Chat memory (multi-turn RAG)  
* ⚡ Streaming responses  
* 🌐 Frontend integration  

---

## 🙌 Acknowledgements

Built as a learning + practical project to understand:

* Backend API design  
* Database integration  
* LLM integration  
* Retrieval-Augmented Generation (RAG)  
* Semantic search using embeddings  

---

## 📜 License

This project is open-source and free to use.

---

⭐ If you found this helpful, consider giving it a star!