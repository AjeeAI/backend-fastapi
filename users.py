import bcrypt
from database import db
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import jwt
import os

from dotenv import load_dotenv
import uvicorn

from middleware import create_token, verify_token

load_dotenv()

app = FastAPI(title="Simple App", version="1.0.0")

token_time = int(os.getenv("token_time"))
class Simple(BaseModel):
    name: str = Field(... , example="Sam Larry")
    email: str = Field(..., example= "sam@email.com")
    password: str = Field(..., example="sam123")
    userType: str = Field(..., example="student")

@app.get("/")
def welcome():
    return "Welcome to Ajee's Api"
@app.post("/signup")
def signUp(input: Simple):
    try:
        duplicate_query = text("""
                               SELECT * FROM users
                               WHERE email= :email
                """)
        existing = db.execute(duplicate_query, {"email": input.email})
        if existing: 
            print("User email already exists!")
            # raise HTTPException(status_code=400, detail="Email already exists")
        query = text("""
                     INSERT INTO users (name, email, password, userType)
                     VALUES (:name, :email, :password, :userType)
                     """)
        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(input.password.encode("utf-8"), salt)
        print(hashedPassword)
        db.execute(query, {"name": input.name, "email": input.email, "password": hashedPassword, "userType": input.userType})
        db.commit()
        return{"message": "User created successfully",
               "data": {"name": input.name, "email": input.email, "userType": input.userType}}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
        
        
class LoginRequest(BaseModel):
    
    email: str = Field(..., example="sam@email.com")
    password: str = Field(..., example="sam123")

@app.post("/login")
def login(input: LoginRequest):
    try:
        query = text("""
            SELECT * FROM users WHERE email = :email
        """)
        result = db.execute(query, {"email": input.email}).mappings().fetchone()
        stored_password = result["password"]

        if not result:
            raise HTTPException(status_code=401, detail="Invalid email or password")

        

        print("Stored password from DB:", stored_password)  # for debugging

        verified_password = bcrypt.checkpw(
            input.password.encode("utf-8"),
            stored_password.encode("utf-8")
        )

        if not verified_password:
            raise HTTPException(status_code=401, detail="Invalid email or password")

        encoded_token = create_token(details= {
            "id": result.id,
            "email": result.email,
            "userType": result.userType,
            "name": result.name
        }, expiry=token_time)
        
        print("User login successful")
        
        return {"message": f"Login successful",
                "token": encoded_token}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
    
# Write a migration file to add gender gender column to the users table


class add_course(BaseModel):
    title: str = Field(..., example = "AI development")
    level: str = Field(..., example = "Beginner")
    
@app.post("/add_courses")
def add_courses(input: add_course, userData = Depends(verify_token)):
    try:
        print(userData)
        if userData["userType"] != 'admin':
            raise HTTPException(status_code=401, detail="You are not authorized to add a course")
        
        query = text("""
            INSERT INTO courses(title, level)
            VALUES (:title, :level)
        """)
        db.execute(query, {"title": input.title, "level": input.level})
        db.commit()
        
        return {
            "message": "Course added successfully",
            "data": {"title": input.title, "level": input.level}
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
class enroll(BaseModel):
    
    courseId: int = Field(..., example=1)
@app.post("/enroll")

def enroll(input: enroll, userData = Depends(verify_token)):
    if userData["userType"] != "student":
        raise HTTPException(status_code=401, detail="You have to be a student to enroll in a course")
    
    query = text("""
                 
                 INSERT INTO enrollments(userId, courseId, studentName) 
                 VALUES (:userId, :courseId, :studentName) 
                 
                 """)
    db.execute(query, {"userId": userData["id"], "courseId": input.courseId, "studentName": userData["name"]})
    
    db.commit()
    
    return {
        "message": "Course enrolled successfully",
        "data": {"userId": userData["id"], "courseId": input.courseId, 
        "studentName": userData["name"]}
    }