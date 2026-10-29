from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify(message="I am IronMan")

@app.get("/health")
def health():
    return jsonify(status="ok")
