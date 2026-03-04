import streamlit as st
import requests
from PIL import Image
import io

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Sentiment and Image Analysis", 
                   layout="centered")

st.title("Sentiment and Image Analysis with FastAPI and Streamlit")
st.write("Upload an image to analyze its sentiment and generate a caption using a FastAPI backend.")  

# defintiion of tabs
tabs = st.tabs(["Text Analysis", "Image Analysis"])

# sentiment analysis
with tabs[0]:
    st.header("Text Sentiment Analysis")

    text_input = st.text_area("Enter text to analyze its sentiment:")
    if st.button("Analyze Sentiment"):
        if not text_input.strip():
            st.warning("Please enter some text to analyze.")
        else:
            with st.spinner("Analyzing sentiment..."):
                try:
                    response = requests.post(f"{API_URL}/predict_sentiment", json={"text": text_input})

                    result = response.json()
                    st.success("Sentiment analysis completed!")
                    st.write(result)
                    
                except Exception as e:
                    st.error(f"Error analyzing sentiment: {e}")

# image analysis
with tabs[1]:
    st.header("Image Analysis")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Image"):
        if uploaded_file is None:
            st.warning("Please upload an image to analyze.")
        else:
            with st.spinner("Analyzing image..."):
                try:
                    # Convert image to bytes
                    img_bytes = io.BytesIO()
                    image.save(img_bytes, format='PNG')
                    img_bytes.seek(0)

                    files = {"image": ("image.png", img_bytes, "image/png")}

                    # Send request to FastAPI backend
                    response = requests.post(f"{API_URL}/predict_image", files=files)

                    result = response.json()
                    st.success("Image analysis completed!")
                    st.write(result)

                except Exception as e:
                    st.error(f"Error analyzing image: {e}")
