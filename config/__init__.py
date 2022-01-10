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
    DB_NAME: str = os.getenv('DB_NAME')



class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()