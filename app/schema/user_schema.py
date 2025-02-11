"""
User Schema
Author: Tom Aston
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.models.user import UserRole


class UserCreateClientRequest(BaseModel):
    """
    client request body for creating a new user
    """

    username: str = Field(max_length=50)
    email: str = Field(max_length=100)
    password: str = Field(min_length=5, max_length=100)
    role: Optional[UserRole] = Field(default=UserRole.USER)


class UserClientResponse(BaseModel):
    """
    client response for getting a user
    """

    id: int
    username: str
    email: str
    role: str
    created: datetime
    updated: datetime


class UserLoginRequest(BaseModel):
    """
    client request body for logging in a user
    """

    email: str
    password: str
