"""
Database
Author: Tom Aston
"""

from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import MetaData

from app.core.config import config_manager


@as_declarative()
class BaseModel:
    metadata = MetaData()
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__.lower()



class Database:
    """
    database class
    """

    def __init__(self, db_url: str) -> None:
        """
        database constructor
        """
        self.engine: AsyncEngine = create_async_engine(
            db_url,
            echo=False,  # set to True to see the SQL queries in the console on fastapi
        )

        self.session_local = async_sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )

    async def create_database(self) -> None:
        """
        create all the database tables defined in models if they don't already exist
        """
        async with self.engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.create_all)

    async def get_db(self) -> AsyncGenerator[AsyncSession, None]:
        """
        get database session
        """
        db: AsyncSession = self.session_local()
        try:
            yield db
        finally:
            await db.close()


database = Database(config_manager.DATABASE_URI)
