"""
Document Model
Author: Tom Aston
"""

from sqlalchemy import TIMESTAMP, Column, Integer, String
from sqlalchemy.sql import func

from app.core.database import BaseModel


class Document(BaseModel):
    """
    document database model
    """

    __tablename__ = "document" # type: ignore

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=False)
    description = Column(String, index=False)
    created = Column(TIMESTAMP, server_default=func.now())

    def __repr__(self) -> str:
        """
        dunder method to return a string representation of the document object
        """
        return f"Document(id={self.id}, title={self.title})"
