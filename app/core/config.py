"""
Config Manager
Author: Tom Aston
"""

import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class ConfigManager(BaseSettings):
    """
    ConfigManager
    """

    # app config-----------------------------------------
    VERSION: str = "0.1.0"
    PROJECT_NAME: str = "doc-similarity-api"
    PROJECT_DESCRIPTION: str = """
    A document similarity API that allows users to create and compare documents
    """

    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # db config-----------------------------------------
    POSTGRES_PASSWORD: str = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_DB: str = os.environ["POSTGRES_DB"]
    POSTGRES_USER: str = os.environ["POSTGRES_USER"]
    POSTGRES_HOST_PORT: str = os.environ["POSTGRES_HOST_PORT"]
    POSTGRES_HOST_NAME: str = os.environ["POSTGRES_HOST_NAME"]
    DB_ENGINE: str = "postgresql"

    DATABASE_URI_FORMAT: str = "{db_engine}+asyncpg://{user}:{password}@{host}:{port}/{database}"

    DATABASE_URI: str = "{db_engine}+asyncpg://{user}:{password}@{host}:{port}/{database}".format(
        db_engine=DB_ENGINE,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST_NAME,
        port=POSTGRES_HOST_PORT,
        database=POSTGRES_DB,
    )

    # security config-----------------------------------------
    JWT_SECRET: str = os.environ["JWT_SECRET"]
    JWT_ALGORITHM: str = os.environ["JWT_ALGORITHM"]
    ACCESS_TOKEN_EXPIRY: int = 3600  # 1 hour
    REFRESH_TOKEN_EXPIRY: int = 3600 * 24 * 2  # 2 days

    # redis config-----------------------------------------
    REDIS_HOST: str = os.environ["REDIS_HOST"]
    REDIS_PORT: int = int(os.environ["REDIS_HOST_PORT"])
    JTI_TOKEN_EXPIRY: int = 3600  # 1 hour
    DOCS_CACHE_EXPIRY: int = 60  # 1 min

    class Config:
        case_sensitive = True


config_manager = ConfigManager()
