'''
Config Manager
Author: Tom Aston
'''
#external dependencies
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

#inbuilt dependencies
import os

load_dotenv()

class ConfigManager(BaseSettings):

    VERSION: str = '1.0.0'

    PROJECT_NAME: str = 'doc-similarity-api'

    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    #db config-----------------------------------------
    POSTGRES_PASSWORD: str = os.environ['POSTGRES_PASSWORD']
    POSTGRES_DB: str = os.environ['POSTGRES_DB']
    POSTGRES_USER: str = os.environ['POSTGRES_USER']
    POSTGRES_HOST_PORT: str = os.environ['POSTGRES_HOST_PORT']
    POSTGRES_HOST_NAME: str = os.environ['POSTGRES_HOST_NAME']
    DB_ENGINE: str = 'postgresql'

    DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"

    DATABASE_URI: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}".format(
        db_engine=DB_ENGINE,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST_NAME,
        port=POSTGRES_HOST_PORT,
        database=POSTGRES_DB,
    )

    class Config:
        case_sensitive = True

config_manager = ConfigManager()