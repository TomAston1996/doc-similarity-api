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
    DocumentUpdateClientRequest,
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
        repository_response: Document | None = await document_repository.get_by_id(
            id, db
        )

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

    async def get_all(self, db: AsyncSession) -> list[DocumentGetByIdClientResponse]:
        """
        service for getting all documents
        """
        repository_response: list[Document] | None = await document_repository.get_all(
            db
        )

        if not repository_response:
            raise HTTPException(status_code=404, detail="No documents found")

        return [
            DocumentGetByIdClientResponse(**doc.__dict__) for doc in repository_response
        ]

    async def update_document(
        self, id: int, document_body: DocumentUpdateClientRequest, db: AsyncSession
    ) -> DocumentCreatedClientResponse:
        """
        service for updating a document
        """
        db_document: Document | None = await document_repository.update_document(
            id=id, document_update_body=document_body, db=db
        )

        if not db_document:
            raise HTTPException(status_code=404, detail="Document not found")

        return DocumentCreatedClientResponse(**db_document.__dict__)

    async def delete_document(self, id: int, db: AsyncSession) -> str:
        """
        service for deleting a document
        """
        db_document: Document | None = await document_repository.delete_document(id, db)

        if not db_document:
            raise HTTPException(status_code=404, detail="Document not found")

        return f"Document [id: {db_document.id}, title: {db_document.title}] deleted successfully"

    async def get_by_title(
        self, title: str, db: AsyncSession
    ) -> DocumentGetByIdClientResponse:
        """
        service for getting a document by title
        """
        repository_response: Document | None = await document_repository.get_by_title(
            title, db
        )

        if not repository_response:
            raise HTTPException(status_code=404, detail="Document not found")

        return DocumentGetByIdClientResponse(**repository_response.__dict__)
