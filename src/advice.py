
import json
from pathlib import Path

# Load advice JSON at module import time
ADVICE_FILE = Path(__file__).parent.parent / "advice.json"

def load_advice():
    """Load the advice JSON file."""
    with open(ADVICE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

_advice_db = load_advice()

def get_advice(disease: str, language: str) -> str:
    """
    Retrieve advice for a given disease and language.
    If the disease is not found, return a generic message.
    """
    disease_key = disease.title()
    if disease_key in _advice_db:
        return _advice_db[disease_key].get(language, _advice_db[disease_key].get("English", "Advice not available."))
    else:
        return f"Advice for '{disease}' not available in {language}."