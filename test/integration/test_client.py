"""
Root Integration Test
Author: Tom Aston
"""

import pytest
from httpx import AsyncClient


class TestRoot:
    """
    Test Root
    """

    @pytest.mark.asyncio
    async def test_client(self, client: AsyncClient):
        """
        Test root
        """
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == "server is running"
