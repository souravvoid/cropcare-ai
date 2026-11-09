# CropCare AI

MVP for Deepavali Build Week (November 2026)

A lightweight Streamlit web app that lets a user upload a crop leaf photograph, validates the image, runs a pretrained MobileNetV2 model for plant disease classification, and provides a cautious prediction with model score, basic advice, and a referral to Krishi Vigyan Kendra (KVK) resources when uncertainty is high.

## Project Structure

```
cropcare/
│
├─ .gitignore          # ignore venv, __pycache__, etc.
├─ README.md           # this file
├─ requirements.txt    # Python dependencies
├─ .venv/              # virtual environment (not tracked)
│
├─ src/
│   ├─ __init__.py
│   ├─ validator.py    # image validation logic
│   ├─ predictor.py    # model loading & inference
│   ├─ decision.py     # decision engine (crop check, uncertainty)
│   ├─ advice.py       # advice retrieval (English/Hindi)
│   └─ referral.py     # KVK referral information
│
└─ streamlit_app.py    # Streamlit UI
```

## Getting Started

```bash
# Clone the repo (or copy files)
git clone https://github.com/souravvoid/cropcare-ai.git
cd cropcare

# Create a virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the app
streamlit run src/streamlit_app.py
```

## Requirements

- Python 3.9+
- Streamlit
- Pillow
- Transformers
- PyTorch (CPU)

## Model

We use the pretrained `LourivalGontijo/plantvillage-mobilenetv2` model from Hugging Face. The model is downloaded automatically on first run and cached using Streamlit's `@st.cache_resource`.

## Limitations

- Model accuracy is high on the training dataset but may vary on real‑world phone photos.
- Only tomato crop is supported in the MVP.
- Advice is generic; for definitive diagnosis consult an agricultural expert.

## License

MIT License.