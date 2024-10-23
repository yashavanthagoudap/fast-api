import requests
from fastapi import HTTPException
from app.config import settings

BASE_URL = "https://api.replicate.com/v1"

def generate_image(prompt: str, model_version: str):
    url = f"{BASE_URL}/predictions"
    headers = {
        "Authorization": f"Token {settings.replicate_api_token}",
        "Content-Type": "application/json"
    }
    data = {
        "version": model_version,
        "input": {
            "prompt": prompt
        }
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Image generation failed.")
    
    result = response.json()
    return result["urls"]["get"]

def fine_tune_model(model_version: str, dataset_url: str):
    url = f"{BASE_URL}/fine-tunes"
    headers = {
        "Authorization": f"Token {settings.replicate_api_token}",
        "Content-Type": "application/json"
    }
    data = {
        "version": model_version,
        "input": {
            "dataset_url": dataset_url
        }
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Fine-tuning failed.")
    
    result = response.json()
    return result

