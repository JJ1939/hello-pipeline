from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify(message="hello from my pipeline")

@app.get("/health")
def health():
    return jsonify(status="ok")
