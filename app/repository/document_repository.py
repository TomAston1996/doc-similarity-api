"""
Document Repository Layer
Author: Tom Aston
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from app.models.document import Document
from app.schema.document_schema import DocumentCreateClientRequest


class DocumentRepository:
    """
    document repository class
    """

    async def get_by_id(self, id: int, db: AsyncSession):
        """
        get a document by id number
        """
        statement = select(Document).where(Document.id == id)
        result = await db.execute(statement)
        return result.scalars().first()

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
