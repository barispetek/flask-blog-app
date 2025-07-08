import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    DEBUG = os.getenv("DEBUG", "True") == "True"

    POSTGRES_DB = os.getenv("POSTGRES_DB", "flask_blog")
    POSTGRES_USER = os.getenv("POSTGRES_USER", "baris")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "yourpassword")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )
