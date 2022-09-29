import os
from typing import Optional

from pydantic import BaseSettings

from dotenv import load_dotenv

if not os.getenv("SQLALCHEMY_DATABASE_URI"):
    load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Book App"
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.getenv("SQLALCHEMY_DATABASE_URI")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

    class Config:
        case_sensitive = True


settings = Settings()
