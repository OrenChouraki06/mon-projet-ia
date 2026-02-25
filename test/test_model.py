# test la fonction get_model() du module model.py
# test la structure de la reponse de predict_sentiment() du module model.py
# test la fonction predict_sentiment() du module model.py

from model import get_model, predict_sentiment

def test_get_model_returns_pipeline():
    model = get_model()

    assert model is not None, "get_model should return a valid model"
    assert hasattr(model, 'predict_proba'), "Model should have a predict_proba method"

def test_predict_sentiment_output_structure():
    input_text = "This is a great product!"
    result = predict_sentiment(input_text)

    assert isinstance(result, dict), "predict_sentiment should return a dictionary"
    assert 'text' in result, "Result should contain 'text' key"
    assert result['text'] == input_text, "The 'text' key should match the input text"
    assert 'label' in result, "Result should contain 'label' key"
    assert isinstance(result['label'], int), "'label' should be an integer"
    assert 'confidence' in result, "Result should contain 'confidence' key"
    assert isinstance(result['confidence'], float), "'confidence' should be a float"
    assert 'predictions' in result, "Result should contain 'predictions' key"
    assert isinstance(result['predictions'], dict), "'predictions' should be a dictionary"
    assert all(isinstance(k, str) for k in result['predictions'].keys()), "Keys in 'predictions' should be strings"
    assert all(isinstance(v, float) for v in result['predictions'].values()), "Values in 'predictions' should be floats"
    assert sum(result['predictions'].values()) > 0.99 and sum(result['predictions'].values()) < 1.01, "The probabilities in 'predictions' should sum to 1"

def test_predict_positive_sentiment():
    input_text = "I love this product!"
    result = predict_sentiment(input_text)

    assert result['label'] == 1, "The label for a positive sentiment should be 1"
    assert result['confidence'] > 0.5, "Confidence for a positive sentiment should be greater than 0.5"

def test_predict_negative_sentiment():
    input_text = "This is the worst experience I've ever had."
    result = predict_sentiment(input_text)

    assert result['label'] == 0, "The label for a negative sentiment should be 0"
    assert result['confidence'] > 0.5, "Confidence for a negative sentiment should be greater than 0.5"
