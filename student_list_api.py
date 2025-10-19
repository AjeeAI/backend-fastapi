from fastapi import FastAPI;
from pydantic import BaseModel;
from dotenv import load_dotenv;
import os;
import uvicorn;

load_dotenv()
app = FastAPI(title = "Simple FastAPI App", version = "1.0.0")


from fastapi.middleware.cors import CORSMiddleware



# Allow frontend origins
origins = [
    "http://localhost:5173",  # Vite default port
    "http://localhost:5174",  # your current port
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/students")
def get_students():
    return [
        {"name": "Adesoji Ajijolaoluwa", "age": 25, "course": "Data Science"},
        {"name": "John Doe", "age": 22, "course": "Computer Science"},
        {"name": "Jane Smith", "age": 23, "course": "Information Technology"},
        {"name": "Emily Johnson", "age": 21, "course": "Software Engineering"},
        {"name": "Michael Brown", "age": 24, "course": "Cybersecurity"},
        {"name": "Sarah Davis", "age": 22, "course": "Web Development"},
        {"name": "David Wilson", "age": 23, "course": "Network Engineering"},
        {"name": "Laura Garcia", "age": 21, "course": "Database Management"},
        {"name": "James Martinez", "age": 25, "course": "Cloud Computing"},
        {"name": "Linda Rodriguez", "age": 24, "course": "Artificial Intelligence"},
        
    ]

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))