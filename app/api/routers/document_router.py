"""
Document Endpoint
Author: Tom Aston
"""

from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import database
from app.schema.document_schema import (
    DocumentCreateClientRequest,
    DocumentCreatedClientResponse,
    DocumentGetByIdClientResponse,
    DocumentUpdateClientRequest,
)
from app.service.document_service import DocumentService

document_router = APIRouter()
document_service = DocumentService()


@document_router.get(
    "/",
    response_model=list[DocumentGetByIdClientResponse],
    status_code=status.HTTP_200_OK,
)
async def get_all_documents(
    db: Annotated[AsyncSession, Depends(database.get_db)],
) -> list[DocumentGetByIdClientResponse]:
    """
    GET all documents endpoint
    """
    return await document_service.get_all(db=db)


@document_router.get(
    "/{id}",
    response_model=DocumentGetByIdClientResponse,
    status_code=status.HTTP_200_OK,
)
async def get_document_by_id(
    id: int, db: Annotated[AsyncSession, Depends(database.get_db)]
) -> DocumentGetByIdClientResponse:
    """
    GET a document by id number endpoint
    """
    return await document_service.get_by_id(id=id, db=db)


@document_router.get(
    "/titles/{title}",
    response_model=DocumentGetByIdClientResponse,
    status_code=status.HTTP_200_OK,
)
async def get_document_by_title(
    title: str, db: Annotated[AsyncSession, Depends(database.get_db)]
) -> DocumentGetByIdClientResponse:
    """
    GET a document by title
    """
    return await document_service.get_by_title(title=title, db=db)


@document_router.post(
    "/",
    response_model=DocumentCreatedClientResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_document(
    document_body: DocumentCreateClientRequest,
    db: Annotated[AsyncSession, Depends(database.get_db)],
) -> DocumentCreatedClientResponse:
    """
    CREATE a new document endpoint
    """
    return await document_service.create_document(document_body=document_body, db=db)


@document_router.patch(
    "/{id}",
    response_model=DocumentCreatedClientResponse,
    status_code=status.HTTP_200_OK,
)
async def update_document(
    id: int,
    document_body: DocumentUpdateClientRequest,
    db: Annotated[AsyncSession, Depends(database.get_db)],
) -> DocumentCreatedClientResponse:
    """
    UPDATE a document by id endpoint
    """
    return await document_service.update_document(
        id=id, document_body=document_body, db=db
    )


@document_router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_document(
    id: int, db: Annotated[AsyncSession, Depends(database.get_db)]
) -> JSONResponse:
    """
    DELETE a document by id endpoint
    """
    response: str = await document_service.delete_document(id=id, db=db)
    return JSONResponse(content={"message": response})
