from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "service": "University Result Portal Sample",
        "message": "Sample portal is running",
        "hostname": socket.gethostname()
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.get("/info")
def info():
    return jsonify({
        "service": "result-portal",
        "environment": os.getenv("APP_ENV", "development")
    })
