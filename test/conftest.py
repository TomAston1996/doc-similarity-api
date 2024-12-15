'''
Test Config
Author: Tom Aston
'''
#ibuilt dependencies
import json
import os

#external dependencies
import pytest
from fastapi.testclient import TestClient

#local dependencies
from app.core.config import config_manager, ConfigManager
from app.main import AppCreator
from app.models.document import Document

@pytest.fixture
def client():
    app_creator = AppCreator()
    app = app_creator.app
    with TestClient(app) as client:
        yield client

@pytest.fixture
def config():
    return ConfigManager()