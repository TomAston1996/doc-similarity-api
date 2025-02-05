"""
Test Config
Author: Tom Aston
"""

import asyncio
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport

from app.core.config import ConfigManager
from app.core.database import database
from app.main import AppCreator


@pytest.fixture(scope="session")
def event_loop():
    """Override the evnt loop"""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Create a new client for each test"""
    app_creator = AppCreator()
    app = app_creator.app
    # Create the app instance here (ensure this is correct for your app)
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac  # Yield the client here so it's passed to the test


@pytest_asyncio.fixture(scope="function")
async def session():
    """Create a fresh database session for each test"""
    async for session in database.get_db():
        yield session


@pytest.fixture
def config():
    return ConfigManager()
