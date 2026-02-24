# Import libs
from flask import Flask, render_template, request

# create application instance
app = Flask(__name__)

# create route
@app.route('/')
def home():
    return "Welcome to the Alyra deployment API!"

@app.route('/health', methods=['GET'])
def health_check():
    return {"status": "healthy", "message": "The API is up and running!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

