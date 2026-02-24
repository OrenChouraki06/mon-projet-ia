from typing import Dict, Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# cache model in memory
_model = None

def train_dummy_model() -> Pipeline:
    """
    Train a dummy model for demonstration purposes.
    In a real application, you would load a pre-trained model from disk.
    """
    # Sample training data
    texts = [
        "I love this product!",
        "This is the worst experience I've ever had.",
        "Amazing service and great quality.",
        "I will never buy this again.",
        "Highly recommend to everyone!",
        "Terrible, do not waste your money."
    ]
    labels = [1, 0, 1, 0, 1, 0]  # 1 for positive, 0 for negative

    # Create a pipeline with TfidfVectorizer and LogisticRegression
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])

    # Train the model
    pipeline.fit(texts, labels)

    return pipeline

def get_model() -> Pipeline:
    """
    Get the trained model. If the model is not already trained, train it.
    """
    global _model
    if _model is None:
        _model = train_dummy_model()
    return _model

def predict_sentiment(text: str) -> Dict[str, Any]:
    """
    Predict the sentiment of the given text using the trained model.
    """
    model = get_model()
    classes = model.classes_

    prediction = model.predict_proba([text])[0]

    best_idx = prediction.argmax()
    label = classes[best_idx]
    confidence = float(prediction[best_idx])

    return {
        "text": text,
        "label": int(label),
        "confidence": confidence,
        "predictions": {str(cls): float(pred) for cls, pred in zip(classes, prediction)}
    }
