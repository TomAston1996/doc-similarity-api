"""
Document Service Layer
Author: Tom Aston
"""

import json
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.cache import add_docs_to_cache, get_docs_from_cache, is_docs_in_cache
from app.errors import DocumentNotFoundException
from app.models.document import Document
from app.repository.document_repository import DocumentRepository
from app.schema.document_schema import (
    DocumentCreateClientRequest,
    DocumentCreatedClientResponse,
    DocumentGetByIdClientResponse,
    DocumentUpdateClientRequest,
)

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
            raise DocumentNotFoundException()

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
        # if the docs are in the cache, return them
        if await is_docs_in_cache("all_docs"):
            json_response = await get_docs_from_cache("all_docs")
            return json.loads(
                json_response, object_hook=lambda d: DocumentGetByIdClientResponse(**d)
            )

        repository_response: list[Document] | None = await document_repository.get_all(
            db
        )

        if not repository_response:
            raise DocumentNotFoundException()

        # add the docs to the cache
        await add_docs_to_cache(
            "all_docs",
            json.dumps([self.__serialize_document(doc) for doc in repository_response]),
        )

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
            raise DocumentNotFoundException()

        return DocumentCreatedClientResponse(**db_document.__dict__)

    async def delete_document(self, id: int, db: AsyncSession) -> str:
        """
        service for deleting a document
        """
        db_document: Document | None = await document_repository.delete_document(id, db)

        if not db_document:
            raise DocumentNotFoundException()

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
            raise DocumentNotFoundException()

        return DocumentGetByIdClientResponse(**repository_response.__dict__)

    def __serialize_document(self, obj: Document) -> dict:
        """
        Convert SQLAlchemy objects to JSON-serializable dictionaries.
        """
        serialized = {}
        for key, value in obj.__dict__.items():
            if key == "_sa_instance_state":  # Skip SQLAlchemy instance state
                continue
            if isinstance(value, datetime):
                serialized[key] = value.isoformat()  # Convert datetime to string
            else:
                serialized[key] = value
        return serialized
