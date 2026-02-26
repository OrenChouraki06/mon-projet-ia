import json
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

def test_health_check():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200, "Health check should return status code 200"

    data = response.get_json()
    assert "status" in data, "Response should contain 'status' key"
    assert data["status"] == "healthy", "Status should be 'healthy'"

def test_predict_route_ok():
    client = app.test_client()
    payload = {
        "text": "I love this product! It's amazing and works perfectly."
    }
    response = client.post('/predict', json=payload)
    assert response.status_code == 200

    data = response.get_json()
    assert "label" in data, "Response should contain 'label' key"
    assert isinstance(data["label"], str), "'label' should be a string"
    assert "confidence" in data, "Response should contain 'confidence' key"
    assert isinstance(data["confidence"], float), "'confidence' should be a float"
    assert "predictions" in data, "Response should contain 'predictions' key"
    assert isinstance(data["predictions"], dict), "'predictions' should be a dict"

def test_predict_route_empty_text():
    client = app.test_client()
    payload = {}
    response = client.post('/predict', json=payload)
    assert response.status_code == 400, "Predict route should return status code 400 when no text is provided"

    data = response.get_json()
    assert "error" in data, "Response should contain 'error' key"
    assert data["error"] == "No text provided", "Error message should indicate that no text was provided"