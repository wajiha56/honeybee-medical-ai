import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API & Security Keys
    WHATSAPP_VERIFY_TOKEN: str = os.getenv("WHATSAPP_VERIFY_TOKEN", "honeybee_secure_token_2026")
    WHATSAPP_APP_SECRET: str = os.getenv("WHATSAPP_APP_SECRET", "default_secret")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    WHATSAPP_TOKEN: str = os.getenv("WHATSAPP_TOKEN", "")
    PHONE_NUMBER_ID: str = os.getenv("PHONE_NUMBER_ID", "")

    # Multi-Lingual Clinical Red Flags (Urdu, Roman Urdu, English)
    TRIAGE_RED_FLAGS: list = [
        "seizure", "fit", "dora", "jhatkay", "jhatke", 
        "breathing", "saans", "chest indrawing", "chati andar",
        "blue", "neela", "unconscious", "behosh"
    ]

    # Database URL (Defaulting to SQLite for local testing)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./medical_engine.db")

settings = Settings()