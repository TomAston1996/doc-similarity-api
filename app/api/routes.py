"""
API Routes
Author: Tom Aston
"""

from fastapi import APIRouter

from app.api.routers.document_router import document_router

routers = APIRouter()

VERSION = "0.1.0"

routers.include_router(
    document_router, prefix=f"/api/{VERSION}/document", tags=["document"]
)
