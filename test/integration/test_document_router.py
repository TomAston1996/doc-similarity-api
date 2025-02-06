"""
Document Router Integration Test
Author: Tom Aston
"""

from datetime import datetime

import pytest
from fastapi import status
from httpx import AsyncClient

from app.core.config import ConfigManager

config_manager = ConfigManager()
VERSION = config_manager.VERSION
DOCUMENT_BASE_URL = f"api/{VERSION}/document/"


class TestDocumentRouter:
    """
    Test Document Router

    #TODO implement test db and set db config in config manager
    """

    @pytest.mark.asyncio
    async def test_create_document(self, client: AsyncClient, session):
        """
        Test creating a document record
        """
        unix_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        test_create_request = {
            "title": f"title_{unix_timestamp}",
            "content": f"content_{unix_timestamp}",
            "description": f"description_{unix_timestamp}",
        }

        print(client)

        response = await client.post(url=DOCUMENT_BASE_URL, json=test_create_request)
        print(response)
        print(response.json())

        response_json = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert response_json["id"] > 0
        assert response_json["title"] == test_create_request["title"]
        assert response_json["content"] == test_create_request["content"]
        assert response_json["description"] == test_create_request["description"]

    @pytest.mark.asyncio
    async def test_get_document_by_id(self, client: AsyncClient):
        """
        Test getting a document record by id
        """
        unix_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        test_create_request = {
            "title": f"title_{unix_timestamp}",
            "content": f"content_{unix_timestamp}",
            "description": f"description_{unix_timestamp}",
        }

        create_response = await client.post(DOCUMENT_BASE_URL, json=test_create_request)

        create_response_json = create_response.json()
        print(create_response_json["id"])

        response = await client.get(f"{DOCUMENT_BASE_URL}{create_response_json['id']}")

        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_json["id"] == create_response_json["id"]
        assert response_json["title"] == create_response_json["title"]
        assert response_json["created"] is not None

    @pytest.mark.asyncio
    async def test_get_all_documents(self, client: AsyncClient):
        """
        Test getting all document records
        """
        response = await client.get(DOCUMENT_BASE_URL)

        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert len(response_json) > 0

    @pytest.mark.asyncio
    async def test_update_document(self, client: AsyncClient):
        """
        Test updating a document record
        """
        unix_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        test_create_request = {
            "title": f"title_{unix_timestamp}",
            "content": f"content_{unix_timestamp}",
            "description": f"description_{unix_timestamp}",
        }

        create_response = await client.post(DOCUMENT_BASE_URL, json=test_create_request)

        create_response_json = create_response.json()

        update_request = {"title": "test_update"}

        update_response = await client.patch(
            f"{DOCUMENT_BASE_URL}{create_response_json['id']}", json=update_request
        )

        update_response_json = update_response.json()

        assert update_response.status_code == status.HTTP_200_OK
        assert update_response_json["id"] == create_response_json["id"]
        assert update_response_json["title"] == update_request["title"]
        assert update_response_json["content"] == create_response_json["content"]
        assert (
            update_response_json["description"] == create_response_json["description"]
        )

    @pytest.mark.asyncio
    async def test_delete_document(self, client: AsyncClient):
        """
        Test deleting a document record
        """
        unix_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        test_create_request = {
            "title": f"title_{unix_timestamp}",
            "content": f"content_{unix_timestamp}",
            "description": f"description_{unix_timestamp}",
        }

        create_response = await client.post(DOCUMENT_BASE_URL, json=test_create_request)

        create_response_json = create_response.json()

        delete_response = await client.delete(
            f"{DOCUMENT_BASE_URL}{create_response_json['id']}"
        )

        get_response = await client.get(
            f"{DOCUMENT_BASE_URL}{create_response_json['id']}"
        )

        assert delete_response.status_code == status.HTTP_200_OK
        assert get_response.status_code == status.HTTP_404_NOT_FOUND
