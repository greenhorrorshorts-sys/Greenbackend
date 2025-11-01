from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

# Load MongoDB connection URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client["Greenshorts"]  # your database name

@app.get("/")
def root():
    return {"message": "✅ Green Horror Backend is live!"}

@app.get("/test-db")
def test_db():
    try:
        client.admin.command("ping")
        return {"message": "✅ Connected to MongoDB successfully!"}
    except Exception as e:
        return {"error": str(e)}

