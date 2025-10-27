import bcrypt
from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import jwt
import os

from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI(title="Simple App", version="1.0.0")

class Simple(BaseModel):
    name: str = Field(... , example="Sam Larry")
    email: str = Field(..., example= "sam@email.com")
    password: str = Field(..., example="sam123")
    userType: str = Field(..., example="student")
    
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

        print("User login successful")
        return {"message": "Login successful"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))