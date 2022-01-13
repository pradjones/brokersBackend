from pydantic import BaseSettings
import os
from dotenv import load_dotenv

env_vars = load_dotenv()

class CommonSettings(BaseSettings):
    APP_NAME: str = "Nelpee Front End"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str = os.getenv('DB_URL')
    DB_USER: str = os.getenv("USER_EMAIL")
    SPACES_PUBLIC_KEY: str = os.getenv("PUBLIC_KEY")
    SPACES_SECRET_KEY: str = os.getenv("SECRET_KEY")



class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    API_VERSION: str = "/api/v1"
    JWT_SECRET: str = "TEST_SECRET_DO_NOT_USE_IN_PRODUCTION"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # Expire in 7 days


settings = Settings()