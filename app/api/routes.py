"""
API Routes
Author: Tom Aston
"""

from fastapi import APIRouter

from app.api.routers.document_router import document_router
from app.core.config import config_manager

routers = APIRouter()

routers.include_router(
    document_router, prefix=f"/api/{config_manager.VERSION}/document", tags=["document"]
)
