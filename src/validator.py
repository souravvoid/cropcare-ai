import io
from PIL import Image
import requests
from io import BytesIO

def validate_image(uploaded_file):
    """
    Validate that the uploaded file is a readable image.
    Returns the PIL Image object in RGB mode or raises ValueError.
    """
    # Check that a file was provided
    if uploaded_file is None:
        raise ValueError("No file uploaded.")
    
    # Read the file bytes
    file_bytes = uploaded_file.read()
    if not file_bytes:
        raise ValueError("Empty file.")
    
    # Try to open with PIL
    try:
        image = Image.open(BytesIO(file_bytes))
        image.verify()  # Verify that it's a valid image
    except Exception as e:
        raise ValueError(f"File is not a valid image: {e}")
    
    # Re-open after verification (PIL needs the file pointer reset)
    file_bytes.seek(0)
    image = Image.open(BytesIO(file_bytes))
    
    # Ensure the image is in RGB mode
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    return image

def check_size(image_bytes, max_mb=5):
    """
    Check that the image size in bytes is below the maximum allowed size.
    """
    size_mb = len(image_bytes) / (1024 * 1024)
    if size_mb > max_mb:
        raise ValueError(f"Image size exceeds {max_mb} MB limit ({size_mb:.2f} MB).")
    return True