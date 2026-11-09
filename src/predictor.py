import torch
from transformers import pipeline
import streamlit as st
from functools import lru_cache

# Cached model loader
@st.cache_resource
def load_model():
    """
    Load the pretrained MobileNetV2 model for plant disease classification.
    Returns a Hugging Face pipeline.
    """
    model_name = "LourivalGontijo/plantvillage-mobilenetv2"
    # Use CPU to avoid memory issues on Streamlit Cloud
    device = -1  # -1 = CPU
    classifier = pipeline(
        "image-classification",
        model=model_name,
        device=device,
        top_k=3,
    )
    return classifier

@st.cache_resource
def get_classifier():
    return load_model()

def predict_disease(image):
    """
    Run inference on the given PIL Image.
    Returns a list of dictionaries with 'label' and 'score' keys.
    """
    classifier = get_classifier()
    # The pipeline expects a list or a single image; we pass the image directly
    predictions = classifier(image)
    # predictions is a list of dicts: [{'label': 'Early Blight', 'score': 0.82}, ...]
    return predictions