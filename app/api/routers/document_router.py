"""
Document Endpoint
Author: Tom Aston
"""

from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import database
from app.core.dependencies import AccessTokenBearer, RoleChecker
from app.core.pagination import Pagination, pagination_params
from app.schema.document_schema import (
    DocumentCreateClientRequest,
    DocumentCreatedClientResponse,
    DocumentGetByIdClientResponse,
    DocumentUpdateClientRequest,
    PaginationClientResponse,
)
from app.service.document_service import DocumentService

document_router = APIRouter()
document_service = DocumentService()

access_token_bearer = AccessTokenBearer()
user_role_checker = RoleChecker(["admin", "user"])
admin_role_checker = RoleChecker(["admin"])


@document_router.get(
    "/",
    response_model=list[DocumentGetByIdClientResponse],
    status_code=status.HTTP_200_OK,
)
async def get_all_documents(
    db: Annotated[AsyncSession, Depends(database.get_db)],
    token: Annotated[dict, Depends(access_token_bearer)],
    _: Annotated[bool, Depends(admin_role_checker)],
) -> list[DocumentGetByIdClientResponse]:
    """
    GET all documents endpoint
    """
    return await document_service.get_all(db=db)


@document_router.get(
    "/paginated",
    response_model=PaginationClientResponse,
    status_code=status.HTTP_200_OK,
)
async def get_all_documents_paginated(
    db: Annotated[AsyncSession, Depends(database.get_db)],
    token: Annotated[dict, Depends(access_token_bearer)],
    _: Annotated[bool, Depends(admin_role_checker)],
    pagination: Annotated[Pagination, Depends(pagination_params)],
) -> PaginationClientResponse:
    """
    GET all documents paginated endpoint
    """
    return await document_service.get_all_paginated(db=db, pagination=pagination)


@document_router.get(
    "/{id}",
    response_model=DocumentGetByIdClientResponse,
    status_code=status.HTTP_200_OK,
)
async def get_document_by_id(
    id: int,
    db: Annotated[AsyncSession, Depends(database.get_db)],
    token: Annotated[dict, Depends(access_token_bearer)],
    _: Annotated[bool, Depends(user_role_checker)],
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
    title: str,
    db: Annotated[AsyncSession, Depends(database.get_db)],
    token: Annotated[dict, Depends(access_token_bearer)],
    _: Annotated[bool, Depends(user_role_checker)],
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
    token: Annotated[dict, Depends(access_token_bearer)],
    _: Annotated[bool, Depends(user_role_checker)],
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
    token: Annotated[dict, Depends(access_token_bearer)],
    _: Annotated[bool, Depends(admin_role_checker)],
) -> DocumentCreatedClientResponse:
    """
    UPDATE a document by id endpoint
    """
    return await document_service.update_document(
        id=id, document_body=document_body, db=db
    )


@document_router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_document(
    id: int,
    db: Annotated[AsyncSession, Depends(database.get_db)],
    token: Annotated[dict, Depends(access_token_bearer)],
    _: Annotated[bool, Depends(user_role_checker)],
) -> JSONResponse:
    """
    DELETE a document by id endpoint
    """
    response: str = await document_service.delete_document(id=id, db=db)
    return JSONResponse(content={"message": response})
