def get_kvk_information():
    """
    Return official KVK referral information.
    In a real deployment this could query a database or API.
    """
    return {
        "title": "Krishi Vigyan Kendra (KVK) Referral",
        "description": "If the model score is low or the prediction is uncertain, farmers should contact their local KVK for expert diagnosis and advice.",
        "website": "https://icar.gov.in/en/krishi-vigyan-kendras",
        "message_en": "The prediction score is low or uncertain. Please consult a local Krishi Vigyan Kendra for expert guidance.",
        "message_hi": "मॉडल स्कोर कम है या अनिश्चितता है। कृपया अपने नजदीकी कृषि विज्ञान केंद्र से संपर्क करें for विशेषज्ञ सलाह।"
    }

def get_referral_message(language: str) -> str:
    """
    Return the appropriate referral message in the selected language.
    """
    info = get_kvk_information()
    return info["message_en"] if language.lower() == "english" else info["message_hi"]