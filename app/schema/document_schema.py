"""
Document Schema
Author: Tom Aston
"""

from datetime import datetime

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


class DocumentGetByIdClientResponse(BaseModel):
    """
    client reponse for getting a document by id
    """

    id: int
    title: str
    created: datetime
