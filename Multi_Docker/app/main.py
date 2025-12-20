import os
import requests
from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel

# env vars
MONGO_URI = os.getenv("MONGO_URI")
OLLAMA_URL = os.getenv("OLLAMA_URL")

# database
client = MongoClient(MONGO_URI)
db = client["chatdb"]
collection = db["question_bank"]    # changed from qa → question_bank

app = FastAPI()

class Query(BaseModel):
    question: str

def ask_ollama(question: str):
    payload = {
        "model": "llama3",
        "prompt": question,
        "stream": False
    }
    r = requests.post(f"{OLLAMA_URL}/api/generate", json=payload)
    data = r.json()
    return data.get("response", "")

@app.post("/ask")
def ask_llm(q: Query):
    answer = ask_ollama(q.question)

    collection.insert_one({
        "question": q.question,
        "answer": answer
    })

    return {"answer": answer}
