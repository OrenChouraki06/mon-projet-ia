# Import libs
from flask import Flask, jsonify, request
from model import predict_sentiment

# create application instance
app = Flask(__name__)

# create route
@app.route('/')
def home():
    return "Welcome to the Alyra deployment API!"

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "The API is up and running!", "config": "uv+pyproject.toml"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = predict_sentiment(text)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

