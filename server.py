from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = client["Greenshorts"]
    client.admin.command("ping")
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
    db = None


# --- Example routes ---
@app.get("/")
def root():
    return {"message": "Welcome to Green Horror Shorts API!"}


@app.get("/test-db")
def test_db():
    if db:
        return {"message": "MongoDB connection is active!"}
    else:
        return {"error": "No database connection"}


# For Vercel compatibility
# (Vercel looks for 'app' object)
@app.get("/api")
def vercel_root():
    return {"status": "API is live and ready for deployment"}

