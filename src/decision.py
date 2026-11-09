from typing import List, Dict, Tuple, Optional

# Supported crops for MVP
SUPPORTED_CROPS = {"Tomato"}

def check_crop(prediction: List[Dict], supported_crop: str) -> bool:
    """
    Determine whether the top prediction belongs to the supported crop.
    For MVP we only consider the top prediction.
    """
    top_label = prediction[0]["label"]
    # The model labels include the crop name; we can check if it contains the crop.
    # The PlantVillage labels are like "Tomato_healthy", "Tomato_early_blight", etc.
    # We'll extract the part before the first underscore.
    crop_name = top_label.split("_")[0].title()
    return crop_name == supported_crop

def check_uncertainty(prediction: List[Dict], score_threshold: float = 0.70) -> bool:
    """
    Determine if the prediction is uncertain.
    - Top score below threshold => uncertain
    - If top-2 scores are too close (difference < 0.10) => uncertain
    """
    top_score = prediction[0]["score"]
    if top_score < score_threshold:
        return True
    # Check second score if exists
    if len(prediction) > 1:
        second_score = prediction[1]["score"]
        if (top_score - second_score) < 0.10:
            return True
    return False

def make_decision(prediction: List[Dict], supported_crop: str, uncertainty_threshold: float = 0.70) -> Tuple[bool, Optional[Dict]]:
    """
    Returns a tuple (is_valid, payload).
    - is_valid: True if we can show the prediction, False if uncertain.
    - payload: the prediction dict if valid, otherwise None.
    """
    if not check_crop(prediction, supported_crop):
        # Prediction is for a different crop => treat as uncertain for MVP
        return False, None
    if check_uncertainty(prediction, uncertainty_threshold):
        return False, None
    return True, prediction[0]  # return top prediction