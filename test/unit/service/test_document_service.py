"""
Unit Test Document Service
Author: Tom Aston
"""

from datetime import datetime
from unittest.mock import AsyncMock, patch

import pytest

from app.models.document import Document
from app.repository.document_repository import DocumentRepository
from app.schema.document_schema import DocumentCreateClientRequest
from app.service.document_service import DocumentService

document_service = DocumentService()


class TestDocumentService:
    """
    Unit Test Document Service
    """

    @pytest.mark.asyncio
    async def test_create_document(self, mock_db_session: AsyncMock):
        """
        Test create document
        """
        created_document = Document(
            id=1,
            title="test",
            content="test",
            description="test",
            created=datetime.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
        )

        with patch.object(
            DocumentRepository,
            "create_document",
            AsyncMock(return_value=created_document),
        ) as mock_repo:
            test_client_request = DocumentCreateClientRequest(
                title="test", content="test", description="test"
            )

            response = await document_service.create_document(
                test_client_request, mock_db_session
            )

            assert response.id == created_document.id
            assert response.title == created_document.title
            assert response.content == created_document.content
            assert response.description == created_document.description
            assert response.created == created_document.created

            # ensure mock was called
            mock_repo.assert_called_once_with(
                document_body=test_client_request, db=mock_db_session
            )

    @pytest.mark.asyncio
    async def test_get_by_id(self, mock_db_session: AsyncMock):
        """
        Test get by id
        """
        document = Document(
            id=1,
            title="test",
            content="test",
            description="test",
            created=datetime.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
        )

        with patch.object(
            DocumentRepository, "get_by_id", AsyncMock(return_value=document)
        ) as mock_repo:
            response = await document_service.get_by_id(1, mock_db_session)

            assert response.id == document.id
            assert response.title == document.title
            assert response.created == document.created

            # ensure mock was called
            mock_repo.assert_called_once_with(1, mock_db_session)

    @pytest.mark.asyncio
    async def test_delete_document(self, mock_db_session: AsyncMock):
        """
        Test delete document
        """
        deleted_document = Document(
            id=1,
            title="test",
            content="test",
            description="test",
            created=datetime.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
        )

        with patch.object(
            DocumentRepository,
            "delete_document",
            AsyncMock(return_value=deleted_document),
        ) as mock_repo:
            response = await document_service.delete_document(1, mock_db_session)

            assert (
                response
                == f"Document [id: {deleted_document.id}, title: {deleted_document.title}] deleted successfully"
            )

            # ensure mock was called
            mock_repo.assert_called_once_with(1, mock_db_session)
