"""
Document Endpoint
Author: Tom Aston
"""

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import database
from app.schema.document_schema import (
    DocumentCreateClientRequest,
    DocumentCreatedClientResponse,
    DocumentGetByIdClientResponse,
)
from app.service.document_service import DocumentService

document_router = APIRouter()
document_service = DocumentService()


@document_router.get("/{id}", response_model=DocumentGetByIdClientResponse)
async def get(
    id: int, db: Annotated[AsyncSession, Depends(database.get_db)]
) -> DocumentGetByIdClientResponse:
    """
    GET a document by id number endpoint
    """
    return await document_service.get_by_id(id=id, db=db)


@document_router.post("/", response_model=DocumentCreatedClientResponse)
async def post(
    document_body: DocumentCreateClientRequest,
    db: Annotated[AsyncSession, Depends(database.get_db)],
) -> DocumentCreatedClientResponse:
    """
    CREATE a new document endpoint
    """
    return await document_service.create_document(document_body=document_body, db=db)
