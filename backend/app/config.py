from pydantic_settings import BaseSettings
from typing import List, Union
import os

class Settings(BaseSettings):
    app_name: str = os.getenv("APP_NAME")
    debug: bool = os.getenv("DEBUG")
    database_url: str = os.getenv("DATABASE_URL")
    cors_origins: Union[List[str], str] = os.getenv("CORS_ORIGINS")
    static_dir: str = os.getenv("STATIC_DIR")
    images_url: str = os.getenv("IMAGES_URL")

    class Config:
        env_file = ".env"

settings = Settings()