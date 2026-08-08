from fastapi import FastAPI
from datetime import datetime
import socket
import os

app = FastAPI(
    title="AWS FastAPI Demo",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI running on AWS! using AWS CICD""
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "development")
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow()
    }

@app.get("/info")
def info():
    return {
        "application": "FastAPI Demo",
        "version": "1.0.0",
        "python": os.sys.version
    }
