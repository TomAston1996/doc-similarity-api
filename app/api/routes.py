"""
API Routes
Author: Tom Aston
"""

from fastapi import APIRouter

from app.api.routers.document_router import document_router
from app.api.routers.user_router import user_router
from app.core.config import config_manager

routers = APIRouter()

routers.include_router(document_router, prefix=f"/api/{config_manager.VERSION}/document", tags=["document"])

routers.include_router(user_router, prefix=f"/api/{config_manager.VERSION}/user", tags=["user"])
