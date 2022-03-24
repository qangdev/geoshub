import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv(".env")


class Settings(BaseSettings):
    API_PREFIX = "/api/v1"
    APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT = os.getenv("APP_PORT", 8000)
    APP_DATABASE_URL = os.getenv("APP_DATABASE_URL", "")
