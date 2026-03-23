import os
from groq import Groq
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column , Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from sentence_transformers import SentenceTransformer
import numpy as np

from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq


from dotenv import load_dotenv    
load_dotenv()


app = FastAPI()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "FastAPI is a modern Python web framework used for building APIs quickly and efficiently.",
    
    "SQLAlchemy is an ORM (Object Relational Mapper) that allows interaction with databases using Python code.",
    
    "RAG stands for Retrieval Augmented Generation, a technique that improves AI responses by providing external context.",
    
    "Large Language Models (LLMs) generate human-like text but may not always have updated or domain-specific knowledge.",
    
    "Python is widely used for backend development, machine learning, and AI applications.",
    
    "In RAG systems, documents are searched first and then passed to the LLM to generate accurate answers.",
]

doc_embeddings = embedding_model.encode(documents)





def search_docs(query):
    query_embedding = embedding_model.encode(query)

    similarities = []

    for i, doc_embedding in enumerate(doc_embeddings):
        similarity = np.dot(query_embedding, doc_embedding) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding)
        )
        similarities.append((similarity, documents[i]))

    similarities.sort(reverse=True)

    return [doc for score, doc in similarities[:3]]




def calculator_tool(query: str):  
    try:
        return str(eval(query))
    except:
        return "Invalid math expression"

def search_tool(query: str):  
    results = search_docs(query)
    return "\n".join(results)



engine = create_engine("sqlite:///users.db", connect_args={"check_same_thread": False}) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class UserDB(Base): 
    __tablename__ = "users"
    id=Column(Integer,primary_key=True,index=True)
    name = Column(String(100), nullable=False)
    score = Column(Integer)

class UserCreate(BaseModel): 
    name: str
    score: int

class UserResponse(BaseModel):
    id: int
    name: str
    score : str 

class PromptRequest(BaseModel):   
    prompt : str


    class Config:
        from_attributes = True

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message":"api is running"}

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
def ask_ai(request : PromptRequest):
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": request.prompt}
            ],
            model="llama-3.3-70b-versatile", 
        )
        return{
            "response": chat_completion.choices[0].message.content
        }


@app.post("/ask-doc")
def ask_doc(request: PromptRequest):

    # 1. Retrieve relevant documents
    relevant_docs = search_docs(request.prompt)

    # 2. Combine context
    context = "\n".join(relevant_docs)

    # 3. Create prompt
    final_prompt = f"""

You are a helpful assistant.

Answer ONLY using the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{request.prompt}
"""

    # 4. Call LLM
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": final_prompt}
        ],
        model="llama-3.3-70b-versatile",
    )

    return {
        "answer": chat_completion.choices[0].message.content,
        "context_used": relevant_docs
    }

llm = ChatGroq(  
    temperature=0, #-----------------------------------> Basically itay amrare koy j kototuk random akta ai hoite pare 
    model_name="llama-3.3-70b-versatile",
    groq_api_key=os.environ.get("GROQ_API_KEY")
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

agent = initialize_agent(  
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


@app.post("/agent")  
def run_agent(request: PromptRequest):
    response = agent.run(request.prompt)
    return {
        "response": response
    }



