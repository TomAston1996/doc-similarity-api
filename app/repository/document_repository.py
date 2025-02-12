"""
Document Repository Layer
Author: Tom Aston
"""

from sqlalchemy import asc, desc, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from app.core.pagination import Pagination, SortEnum
from app.models.document import Document
from app.schema.document_schema import (
    DocumentCreateClientRequest,
    DocumentUpdateClientRequest,
)


class DocumentRepository:
    """
    document repository class
    """

    async def get_all(self, db: AsyncSession) -> list[Document] | None:
        """
        get all documents
        """
        statement = select(Document).order_by(Document.id)
        result = await db.execute(statement)
        return result.scalars().all()

    async def get_all_paginated(
        self, db: AsyncSession, pagination: Pagination
    ) -> tuple[list[Document], int] | None:
        """
        get all documents paginated

        Returns:
        - list of documents
        - total count of documents
        """
        order = desc if pagination.order == SortEnum.DESC else asc
        statement = (
            select(Document)
            .limit(pagination.perPage)
            .offset(
                pagination.page - 1
                if pagination.page == 1
                else (pagination.page - 1) * pagination.perPage
            )
            .order_by(order(Document.id))
        )
        result = await db.execute(statement)
        count_result = await db.execute(
            select(func.count()).select_from(select(Document.id).subquery())
        )
        count = count_result.scalar_one()
        return (result.scalars().all(), count)

    async def get_by_id(self, id: int, db: AsyncSession) -> Document | None:
        """
        get a document by id number
        """
        statement = select(Document).where(Document.id == id)
        result = await db.execute(statement)
        return result.scalars().first()

    async def get_by_title(self, title: str, db: AsyncSession) -> Document | None:
        """
        get all documents by title
        """
        statement = select(Document).where(Document.title == title)
        result = await db.execute(statement)
        return result.scalars().first()

    async def update_document(
        self,
        id: int,
        document_update_body: DocumentUpdateClientRequest,
        db: AsyncSession,
    ) -> Document:
        """
        update a document by id
        """
        db_document = await self.get_by_id(id, db)

        if not db_document:
            return None

        for key, value in document_update_body.model_dump().items():
            if value is not None:
                setattr(db_document, key, value)

        await db.commit()
        await db.refresh(db_document)

        return db_document

    async def create_document(
        self, document_body: DocumentCreateClientRequest, db: AsyncSession
    ) -> Document:
        """
        create a new document
        """
        db_document = Document(**document_body.model_dump())
        db.add(db_document)
        await db.commit()
        await db.refresh(db_document)  # Refresh to get auto-generated fields like 'id'
        return db_document

    async def delete_document(self, id: int, db: AsyncSession) -> Document | None:
        """
        delete a document by id
        """
        db_document = await self.get_by_id(id, db)

        if not db_document:
            return None

        await db.delete(db_document)
        await db.commit()

        return db_document
