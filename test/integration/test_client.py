"""
Root Integration Test
Author: Tom Aston
"""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_client(client: AsyncClient, session):
    """
    Test root
    """
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == "server is running"
