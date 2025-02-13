"""
User Model
Author: Tom Aston
"""

from enum import Enum

from sqlalchemy import TIMESTAMP, Column, Integer, String, Enum as SQLEnum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import BaseModel


class UserRole(Enum):
    """
    User Role Enum
    """

    ADMIN = "admin"
    USER = "user"


class User(BaseModel):
    """
    User database model
    """

    __tablename__ = "user"  # type: ignore

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    password_hash = Column(String, index=False)
    created = Column(TIMESTAMP, server_default=func.now())
    updated = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    role = Column(SQLEnum(UserRole), nullable=False, default=UserRole.USER)

    documents = relationship("Document", back_populates="owner")

    def __repr__(self) -> str:
        """
        dunder method to return a string representation of the user object
        """
        return f"User(id={self.id}, username={self.username})"
