"""
User Schema
Author: Tom Aston
"""

from datetime import datetime

from pydantic import BaseModel, Field


class UserCreateClientRequest(BaseModel):
    """
    client request body for creating a new user
    """

    username: str = Field(max_length=50)
    email: str = Field(max_length=100)
    password: str = Field(min_length=5, max_length=100)


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
