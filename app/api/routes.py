from fastapi import APIRouter

from app.api.routers.document_router import router as document_router

routers = APIRouter()
router_list = [document_router]

for router in router_list:
    routers.include_router(router)