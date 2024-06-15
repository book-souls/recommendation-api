from flask import Flask, jsonify, request 
import fasttext

app = Flask(__name__)

model = fasttext.load_model("model.bin")

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

    prediction = model.get_sentence_vector(input)
    return jsonify(prediction.tolist())

@app.route("/flask-health-check")
def flask_health_check():
	return "success"
