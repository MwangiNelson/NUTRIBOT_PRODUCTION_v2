from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/generate-text', methods=['POST'])
def generate_text():
    input_text = request.json.get('text')
    response = requests.post(
        "https://api-inference.huggingface.co/models/NelsonKamau47/NutriBotV2",
        headers={"Authorization": "Bearer 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"},
        json={"inputs": input_text, "parameters": {"max_length": 50}}
    )
    if response.status_code == 200:
        return jsonify(response.json()[0]['generated_text'])
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
