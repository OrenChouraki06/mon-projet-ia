#import des bibliothèques nécessaires
import tensorflow as tf

# chargement du modèle
def load_model(model_path):
    return tf.keras.models.load_model(model_path)

# fonction de prédiction
def predict(model, image):
    prediction = model.predict(image)
    return prediction.tolist()