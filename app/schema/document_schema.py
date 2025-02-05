"""
Document Schema
Author: Tom Aston
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DocumentCreateClientRequest(BaseModel):
    """
    client request body for creating a new document
    """

    title: str
    content: str
    description: str


class DocumentCreatedClientResponse(BaseModel):
    """
    client reponse for creating a new document
    """

    id: int
    title: str
    content: str
    description: str
    created: datetime


class DocumentUpdateClientRequest(BaseModel):
    """
    client request body for updating a document
    """

    title: Optional[str] = None
    content: Optional[str] = None
    description: Optional[str] = None


class DocumentGetByIdClientResponse(BaseModel):
    """
    client reponse for getting a document by id
    """

    id: int
    title: str
    created: datetime
