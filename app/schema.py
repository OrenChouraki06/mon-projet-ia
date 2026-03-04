from pydantic import BaseModel

class ImagePrediction(BaseModel):
    Number: int
    Proba: dict

class SentimentPrediction(BaseModel):
    Proba: Dict[str, float]
    Sentiment: str
    Confidence: float

class SentimentRequest(BaseModel):
    text: str
