from datetime import datetime
from typing import Optional

def get_firebase_config():
    print("ℹ️  Firebase not needed - using print-based forwarding")
    return None

def initialize_firebase():
    print("ℹ️  Firebase not needed - using print-based forwarding")
    return None

def get_db():
    print("ℹ️  Firebase not needed - using print-based forwarding")
    return None

def save_unanswered_question(question_english):
    try:
        print(f"forwarded to doctor: {question_english}")
    except Exception as e:
        print(f"❌ Error in forwarding logic: {str(e)}")
        raise e

def save_user_interaction(question_english, answer_english, user_session_id=None):
    try:
        print(f"User interaction logged: Q: {question_english[:50]}... A: {answer_english[:50]}...")
        
        # Check if this was a forwarded question
        unanswered_indicators = [
            "doctor has been notified",
            "doctor will be notified", 
            "check back in a few days",
            "unable to answer your question"
        ]
        
        if any(indicator in answer_english.lower() for indicator in unanswered_indicators):
            print(f"forwarded to doctor: {question_english}")
        
    except Exception as e:
        print(f"❌ Error in interaction logging: {str(e)}")
        raise e
