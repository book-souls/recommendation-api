from flask import Flask, jsonify, request
from model import get_sentence_vector

app = Flask(__name__)

@app.route("/vectorize", methods=["POST"])
def vectorize():
    body = request.json
    if not body:
        return jsonify({"error": "Request body is required"}), 400

    input = body.get("input")
    if not input:
        return jsonify({"error": "'input' not found in body"}), 400

    if not isinstance(input, str):
        return jsonify({"error": "'input' must be a string"}), 400

    embedding = get_sentence_vector(input)
    return jsonify(embedding)

@app.route("/flask-health-check")
def flask_health_check():
	return "success"
