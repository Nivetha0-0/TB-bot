import os
import json
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

def get_secret(key: str) -> str:
    """
    Get a secret value from either environment variables (local) or Streamlit secrets (deployed)
    """
    # First try to get from environment variables (for local development)
    env_value = os.getenv(key)
    if env_value:
        return env_value
    
    # If not found in environment, try Streamlit secrets (for deployed version)
    try:
        import streamlit as st
        return st.secrets[key]
    except (ImportError, KeyError):
        raise ValueError(f"Secret '{key}' not found in environment variables or Streamlit secrets")

def get_json_secret(key: str) -> dict:
    """
    Get a JSON secret value from either environment variables or Streamlit secrets
    """
    value = get_secret(key)
    try:
        if isinstance(value, str):
            return json.loads(value)
        return value
    except json.JSONDecodeError:
        raise ValueError(f"Secret '{key}' is not valid JSON")

# Configuration getters
def get_openai_key() -> str:
    return get_secret("OPENAI_KEY")

def get_mongodb_uri() -> str:
    return get_secret("MONGODB_URI")

def get_google_cloud_project() -> str:
    return get_secret("GOOGLE_CLOUD_PROJECT")

def get_google_application_credentials() -> dict:
    return get_json_secret("GOOGLE_APPLICATION_CREDENTIALS")

def get_firebase_service_account_key() -> dict:
    # Firebase is no longer used - this function is kept for backward compatibility
    return {} 