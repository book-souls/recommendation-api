from flask import Flask, jsonify, request 
import fasttext

app = Flask(__name__)

model = fasttext.load_model("model.bin")

@app.route("/vectorize")
def index():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "'text' query parameter is required"}), 400
 
    prediction = model.get_sentence_vector(text)
    return jsonify(prediction.tolist())

@app.route("/flask-health-check")
def flask_health_check():
	return "success"
