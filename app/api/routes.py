'''
API Routes
Author: Tom Aston
'''

#external dependencies
from fastapi import APIRouter

#local dependencies
from app.api.routers.document_router import router as document_router

routers = APIRouter()
router_list = [document_router]

for router in router_list:
    routers.include_router(router)