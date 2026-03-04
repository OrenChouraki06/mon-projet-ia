# import librairies
import numpy as np
from PIL import Image
import io

# convert image en tableau numpy, redimensionner, convertir en noir et blanc, normaliser
def preprocess_image(image_bytes):
    try:
        # Convertir les bytes en image PIL
        image = Image.open(io.BytesIO(image_bytes))

         # Redimensionner à 28x28
        image = image.resize((28, 28))

        # convertir en noir et blanc
        image_black = image.convert('L')

         # Convertir en tableau numpy
        image_array = np.array(image_black)
        
        # reshape et normalisation 
        image_final = image_array.reshape(1, 28 * 28) / 255.0
    
        return image_final
    except Exception as e:
        raise ValueError(f"Error preprocessing image: {str(e)}")