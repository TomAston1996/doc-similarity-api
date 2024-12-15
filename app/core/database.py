'''
Database
Author: Tom Aston
'''

#external dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base, declared_attr, as_declarative
from typing import Any, Generator

#local dependencies
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
    pass

    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(db_url, echo=True)
        self.session_local = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def create_database(self) -> None:
        '''
        create all the database tables defined in models if they don't already exist
        '''
        BaseModel.metadata.create_all(bind=self.engine)

    def get_db(self) -> Generator[Session, Any, None]:
        '''
        get database session
        '''
        db: Session = self.session_local()
        try:
            yield db
        finally:
            db.close()

database = Database(config_manager.DATABASE_URI)