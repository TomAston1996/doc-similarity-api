"""
Database
Author: Tom Aston
"""

# external dependencies
from typing import Any, AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

# local dependencies
from app.core.config import config_manager


@as_declarative()
class BaseModel:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class Database:
    """
    Database class
    """

    def __init__(self, db_url: str) -> None:
        self.engine = AsyncEngine(
            create_engine(
                url=config_manager.DATABASE_URI,
                echo=False,  # set to True to see the SQL queries in the console on fastapi
            )
        )

        self.session_local = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine, expire_on_commit=False
        )

    def create_database(self) -> None:
        """
        create all the database tables defined in models if they don't already exist
        """
        BaseModel.metadata.create_all(bind=self.engine)

    async def get_db(self) -> AsyncGenerator[AsyncSession, None]:
        """
        get database session
        """
        db: AsyncSession = self.session_local()
        try:
            yield db
        finally:
            db.close()


database = Database(config_manager.DATABASE_URI)
