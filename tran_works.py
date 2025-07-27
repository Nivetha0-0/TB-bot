import os
import json
import tempfile
from google.cloud import translate 
from google.cloud import texttospeech 
from google.cloud import speech 
from typing import Optional, List, Type, TypeVar
from config import get_google_application_credentials, get_google_cloud_project

GCClient = TypeVar('GCClient')
_translator_client = None
_texttospeech_client = None
_speech_client = None

def _initialize_gc_client(client_class: Type[GCClient]) -> Optional[GCClient]:
    try:
        # Get service account credentials from config
        service_account_info = get_google_application_credentials()
        
        # Create temporary file with credentials
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
            json.dump(service_account_info, temp_file)
            temp_credentials_path = temp_file.name
        
        # Set the environment variable
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = temp_credentials_path
        
        client = client_class()
        
        # Don't delete the temp file immediately - keep it for the session
        # The file will be cleaned up when the process ends
        
        return client
    except Exception as e:
        print(f"Error initializing Google Cloud {client_class.__name__}: {e}")
        return None

def get_translator_client() -> Optional[translate.TranslationServiceClient]:
    global _translator_client
    if _translator_client is None:
        _translator_client = _initialize_gc_client(translate.TranslationServiceClient)
    return _translator_client

def get_texttospeech_client() -> Optional[texttospeech.TextToSpeechClient]:
    global _texttospeech_client
    if _texttospeech_client is None:
        _texttospeech_client = _initialize_gc_client(texttospeech.TextToSpeechClient)
    return _texttospeech_client

def get_speech_client() -> Optional[speech.SpeechClient]:
    global _speech_client
    if _speech_client is None:
        _speech_client = _initialize_gc_client(speech.SpeechClient)
    return _speech_client

def get_supported_languages(client, allowed_langs: Optional[List[str]] = None) -> dict[str, str]:
    if not client:
        return {}
    try:
        project_id = get_google_cloud_project()
        parent = f"projects/{project_id}/locations/global"
        response = client.get_supported_languages(parent=parent, display_language_code='en')

        languages = {}
        for lang in response.languages:
            if allowed_langs and lang.language_code not in allowed_langs:
                continue

            display_name = lang.display_name if lang.display_name else lang.language_code
            languages[lang.language_code] = display_name
        return languages
    except Exception as e:
        print(f"Error fetching supported languages (V3): {e}")
        return {}

def translate_text(client, text: Optional[str], target_language_code: str, source_language_code: str) -> Optional[str]:
    if not text or not client:
        return text

    if source_language_code == target_language_code:
        return text

    try:
        project_id = get_google_cloud_project()
        parent = f"projects/{project_id}/locations/global"
        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [text],
                "mime_type": "text/plain",
                "source_language_code": source_language_code,
                "target_language_code": target_language_code,
            }
        )
        translated_text = response.translations[0].translated_text
        return translated_text
    except Exception as e:
        print(f"Error translating text (V3): {e}")
        return None

# Helper functions to access other secrets
def get_openai_key() -> str:
    from config import get_openai_key as config_get_openai_key
    return config_get_openai_key()

def get_mongodb_uri() -> str:
    from config import get_mongodb_uri as config_get_mongodb_uri
    return config_get_mongodb_uri()

def get_firebase_service_account_key():
    from config import get_firebase_service_account_key as config_get_firebase_key
    return config_get_firebase_service_account_key()

def get_google_cloud_project() -> str:
    from config import get_google_cloud_project as config_get_google_project
    return config_get_google_project()
