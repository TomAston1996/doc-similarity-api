"""
Document Service Layer
Author: Tom Aston
"""

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.repository.document_repository import DocumentRepository
from app.schema.document_schema import (
    DocumentCreateClientRequest,
    DocumentCreatedClientResponse,
    DocumentGetByIdClientResponse,
)
from app.models.document import Document

document_repository = DocumentRepository()


class DocumentService:
    """
    document service class
    """

    async def get_by_id(
        self, id: int, db: AsyncSession
    ) -> DocumentGetByIdClientResponse:
        """
        service for getting a document by id number
        """
        repository_response: Document | None = await document_repository.get_by_id(id, db)

        if not repository_response:
            raise HTTPException(status_code=404, detail="Document not found")

        return DocumentGetByIdClientResponse(**repository_response.__dict__)

    async def create_document(
        self, document_body: DocumentCreateClientRequest, db: AsyncSession
    ) -> DocumentCreatedClientResponse:
        """
        service for a creating document
        """
        db_document: Document = await document_repository.create_document(
            document_body=document_body, db=db
        )

        return DocumentCreatedClientResponse(**db_document.__dict__)
