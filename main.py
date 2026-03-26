import math
import os
from functools import lru_cache
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

load_dotenv()

app = FastAPI(title="Chatbot API", version="1.0.0")

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'users.db'}")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

DOCUMENTS = [
    "FastAPI is a modern Python web framework used for building APIs quickly and efficiently.",
    "SQLAlchemy is an ORM (Object Relational Mapper) that allows interaction with databases using Python code.",
    "RAG stands for Retrieval Augmented Generation, a technique that improves AI responses by providing external context.",
    "Large Language Models (LLMs) generate human-like text but may not always have updated or domain-specific knowledge.",
    "Python is widely used for backend development, machine learning, and AI applications.",
    "In RAG systems, documents are searched first and then passed to the LLM to generate accurate answers.",
]


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    score = Column(Integer)


class UserCreate(BaseModel):
    name: str
    score: int


class PromptRequest(BaseModel):
    prompt: str


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def require_groq_api_key() -> str:
    if not GROQ_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY is not configured. Set it in the deployment environment.",
        )
    return GROQ_API_KEY


@lru_cache(maxsize=1)
def get_groq_client():
    from groq import Groq

    return Groq(api_key=require_groq_api_key())


@lru_cache(maxsize=1)
def get_embedding_model():
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer("all-MiniLM-L6-v2")


@lru_cache(maxsize=1)
def get_doc_embeddings():
    return get_embedding_model().encode(DOCUMENTS)


def search_docs(query: str):
    query_embedding = get_embedding_model().encode(query)
    doc_embeddings = get_doc_embeddings()
    similarities = []

    for i, doc_embedding in enumerate(doc_embeddings):
        similarity = np.dot(query_embedding, doc_embedding) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding)
        )
        similarities.append((similarity, DOCUMENTS[i]))

    similarities.sort(reverse=True)
    return [doc for score, doc in similarities[:3]]


def calculator_tool(query: str):
    try:
        return str(eval(query, {"__builtins__": None}, {"math": math}))
    except Exception:
        return "Invalid math expression"


def search_tool(query: str):
    return "\n".join(search_docs(query))


@lru_cache(maxsize=1)
def get_agent_executor():
    from langchain.agents import AgentType, initialize_agent
    from langchain_core.tools import Tool
    from langchain_groq import ChatGroq

    llm = ChatGroq(
        temperature=0,
        model_name=GROQ_MODEL,
        groq_api_key=require_groq_api_key(),
    )

    tools = [
        Tool(
            name="Calculator",
            func=calculator_tool,
            description="Use this for math calculations like 25 * 4",
        ),
        Tool(
            name="Document Search",
            func=search_tool,
            description="Use this to answer questions from documents",
        ),
    ]

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
    )


@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "database": "configured",
        "groq_api_key_configured": bool(GROQ_API_KEY),
    }


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(UserDB).all()


@app.get("/users/top")
def filter_users(db: Session = Depends(get_db)):
    users = db.query(UserDB).filter(UserDB.score > 80).order_by(UserDB.score.desc()).all()
    return [user.name for user in users]


@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = UserDB(name=user.name, score=user.score)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User added successfully", "user": new_user}


@app.post("/ask-ai")
def ask_ai(request: PromptRequest):
    chat_completion = get_groq_client().chat.completions.create(
        messages=[{"role": "user", "content": request.prompt}],
        model=GROQ_MODEL,
    )
    return {"response": chat_completion.choices[0].message.content}


@app.post("/ask-doc")
def ask_doc(request: PromptRequest):
    relevant_docs = search_docs(request.prompt)
    context = "\n".join(relevant_docs)

    final_prompt = f"""
You are a helpful assistant.

Answer ONLY using the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{request.prompt}
"""

    chat_completion = get_groq_client().chat.completions.create(
        messages=[{"role": "user", "content": final_prompt}],
        model=GROQ_MODEL,
    )

    return {
        "answer": chat_completion.choices[0].message.content,
        "context_used": relevant_docs,
    }


@app.post("/agent")
def run_agent(request: PromptRequest):
    response = get_agent_executor().invoke({"input": request.prompt})
    return {"response": response}


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
