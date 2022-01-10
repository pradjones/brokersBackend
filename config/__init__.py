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
    # DB_URL: str = os.getenv('DB_URL')
    # DB_NAME: str = os.getenv('DB_NAME')
    DB_URL: str = "mongodb+srv://pradjones:Visagio2020!@cluster0.jwkit.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DB_NAME: str = "Nelpee"



class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()