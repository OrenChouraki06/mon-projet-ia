# import des librairies
import fastapi
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from pydantic import BaseModel
import numpy as np

from model import load_model, predict
from preprocess import preprocess_image

from typing import Dict

from model_bert import Model, get_model

# creatiobn de l'instance de l'application FastAPI
app = FastAPI()

# chargement du modèle au demarrage de l'application
model = load_model("model/model_alyra_0.1.0.h5")

class ImagePrediction(BaseModel):
    Number: int
    Proba: dict

class SentimentPrediction(BaseModel):
    Proba: Dict[str, float]
    Sentiment: str
    Confidence: float

class SentimentRequest(BaseModel):
    text: str

# creation des routes de l'API
@app.get("/")
def root():
    return {"message": "Welcome to the Alyra deployment FASTAPI!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "The API is up and running!"}

@app.post("/predict_image", response_model=ImagePrediction)
async def predict_image(file: UploadFile = File(...)):
    try:
        image = await file.read()
        preprocess_image = preprocess_image(image)
        prediction = predict(model, preprocess_image)
        round_prediction = {i: round(p, 2) for i, p in enumerate(prediction)}

        return {
            "Number": int(np.argmax(prediction[0])),
            "Proba": round_prediction
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")
    
@app.post("/predict_sentiment", response_model=SentimentPrediction)
async def predict_bert(request: SentimentRequest, model: Model = Depends(get_model)):
    try:
        sentiment, confidence, proba = model.predict(request.text)

        return {
            "Proba": proba,
            "Sentiment": sentiment,
            "Confidence": confidence
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")