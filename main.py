import os
import math
import numpy as np
import traceback
from dotenv import load_dotenv

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from groq import Groq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from langchain_core.tools import Tool
# FIX 2: Use create_react_agent instead of deprecated initialize_agent
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_groq import ChatGroq

import uvicorn  # FIX 1: needed for dynamic port binding

# ------------------ ENV ------------------
load_dotenv()

# ------------------ FASTAPI ------------------
app = FastAPI()

# ------------------ GROQ CLIENT ------------------
client = Groq(
    api_key=os.environ["GROQ_API_KEY"],
)

# ------------------ EMBEDDINGS ------------------
vectorizer = TfidfVectorizer()

documents = [
    "FastAPI is a modern Python web framework used for building APIs quickly and efficiently.",
    "SQLAlchemy is an ORM (Object Relational Mapper) that allows interaction with databases using Python code.",
    "RAG stands for Retrieval Augmented Generation, a technique that improves AI responses by providing external context.",
    "Large Language Models (LLMs) generate human-like text but may not always have updated or domain-specific knowledge.",
    "Python is widely used for backend development, machine learning, and AI applications.",
    "In RAG systems, documents are searched first and then passed to the LLM to generate accurate answers.",
]

doc_vectors = vectorizer.fit_transform(documents)

# ------------------ SEARCH ------------------
def search_docs(query):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, doc_vectors).flatten()
    top_indices = similarities.argsort()[-3:][::-1]
    return [documents[i] for i in top_indices]

# ------------------ TOOLS ------------------
# FIX 3: Replaced unsafe eval() with simpler expression parser using ast
import ast
import operator

SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

def safe_eval(node):
    if isinstance(node, ast.Constant):
        return node.n
    elif isinstance(node, ast.BinOp):
        op = SAFE_OPERATORS.get(type(node.op))
        if op is None:
            raise ValueError("Unsupported operator")
        return op(safe_eval(node.left), safe_eval(node.right))
    elif isinstance(node, ast.UnaryOp):
        op = SAFE_OPERATORS.get(type(node.op))
        if op is None:
            raise ValueError("Unsupported operator")
        return op(safe_eval(node.operand))
    else:
        raise ValueError("Unsupported expression")

def calculator_tool(query: str):
    try:
        tree = ast.parse(query, mode="eval")
        result = safe_eval(tree.body)
        return str(result)
    except Exception:
        return "Invalid math expression"

def search_tool(query: str):
    results = search_docs(query)
    return "\n".join(results)

# ------------------ DATABASE ------------------
engine = create_engine("sqlite:///users.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
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

# ------------------ ROUTES ------------------
@app.get("/")
def root():
    return {"message": "API is running 🚀"}

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

# ------------------ BASIC AI ------------------
@app.post("/ask-ai")
def ask_ai(request: PromptRequest):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": request.prompt}],
        model="llama-3.3-70b-versatile",
    )
    return {"response": chat_completion.choices[0].message.content}

# ------------------ RAG ------------------
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

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": final_prompt}],
        model="llama-3.3-70b-versatile",
    )

    return {
        "answer": chat_completion.choices[0].message.content,
        "context_used": relevant_docs
    }

# ------------------ AGENT ------------------
llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile",
    groq_api_key=os.environ["GROQ_API_KEY"],
)

tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Use this for math calculations like 25 * 4"
    ),
    Tool(
        name="Document Search",
        func=search_tool,
        description="Use this to answer questions from documents"
    )
]

# FIX 2: Updated to use non-deprecated create_react_agent
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

@app.post("/agent")
def run_agent(request: PromptRequest):
    try:
        response = agent_executor.invoke({"input": request.prompt})
        return {"response": response["output"]}
    except Exception as e:
        return {"error": str(e)}


# FIX 1: Bind to Railway's dynamic PORT env variable
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)