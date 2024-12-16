'''
Document Endpoint
Author: Tom Aston
'''

#external dependencies
from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session

#local dependencies
from app.schema.document_schema import DocumentCreatedClientResponse, DocumentCreateClientRequest, DocumentGetByIdClientResponse
from app.core.database import database
from app.service import document_service

router = APIRouter(
    prefix='/document',
    tags=['document']
)

@router.get('/{id}', response_model=DocumentGetByIdClientResponse)
async def get(id: int, db: Annotated[Session, Depends(database.get_db)]) -> DocumentGetByIdClientResponse:
    '''
    GET a document by id number endpoint
    '''
    return await document_service.get_by_id(id=id, db=db)


@router.post('', response_model=DocumentCreatedClientResponse)
async def post(document_body: DocumentCreateClientRequest, db: Annotated[Session, Depends(database.get_db)]) -> DocumentCreatedClientResponse:
    '''
    CREATE a new document endpoint
    '''
    return await document_service.create_document(document_body=document_body, db=db)