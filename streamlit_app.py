import streamlit as st
from PIL import Image
import io

from src.validator import validate_image, check_size
from src.predictor import predict_disease
from src.decision import check_crop, check_uncertainty, make_decision
from src.advice import get_advice
from src.referral import get_referral_message

st.set_page_config(page_title="CropCare AI", layout="centered")

st.title("🌿 CropCare AI")
st.caption("AI-assisted crop disease screening – upload a leaf photo and get a cautious prediction.")

# Language selection
language = st.selectbox("Select language", ["English", "Hindi"])

# Crop selection (MVP: Tomato only)
crop = st.selectbox("Select crop", ["Tomato"])

# Image uploader
uploaded_file = st.file_uploader(
    "Upload a crop leaf photograph",
    type=["jpg", "jpeg", "png"],
    help="JPG, JPEG or PNG · Maximum 5 MB"
)

if uploaded_file is not None:
    try:
        # Validate image
        image_bytes = uploaded_file.read()
        validate_image(io.BytesIO(image_bytes))  # will raise if invalid
        # Re-load bytes for size check
        image_bytes.seek(0)
        check_size(image_bytes, max_mb=5)

        # Convert to PIL Image for prediction
        pil_image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # Run prediction
        predictions = predict_disease(pil_image)

        # Decision logic
        valid, top_pred = make_decision(predictions, supported_crop=crop, uncertainty_threshold=0.70)

        if valid:
            # Show prediction
            st.subheader("Prediction")
            st.write(f"**Likely disease:** {top_pred['label']}")
            st.write(f"**Model score:** {top_pred['score']:.0%}")

            # Show advice
            disease_name = top_pred['label'].split('_')[0].title()
            advice_text = get_advice(disease_name, language)
            st.subheader("Advice")
            st.write(advice_text)

        else:
            # Uncertain or wrong crop – show referral
            st.warning("Uncertain prediction or unsupported crop.")
            st.subheader("Next Steps")
            referral_msg = get_referral_message(language)
            st.write(referral_msg)
            st.markdown(f"[Official KVK directory]({__import__('src.referral').referral.get_kvk_information()['website']})")

    except Exception as e:
        # Validation error
        st.error(f"Image validation failed: {e}")

# Footer
st.caption("This is an experimental AI screening tool. It is not a confirmed diagnosis. For definitive identification, consult an agricultural expert.")