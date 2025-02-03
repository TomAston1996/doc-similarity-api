'''
Test Config
Author: Tom Aston
'''
#external dependencies
import pytest
from fastapi.testclient import TestClient

#local dependencies
from app.core.config import ConfigManager
from app.main import AppCreator

@pytest.fixture
def client():
    app_creator = AppCreator()
    app = app_creator.app
    with TestClient(app) as client:
        yield client

@pytest.fixture
def config():
    return ConfigManager()