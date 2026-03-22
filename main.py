import os
from groq import Groq
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column , Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


from dotenv import load_dotenv    
load_dotenv()


app = FastAPI()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)




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



