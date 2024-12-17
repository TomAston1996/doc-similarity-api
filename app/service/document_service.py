'''
Document Service Layer
Author: Tom Aston
'''

#external dependencies
from sqlalchemy.orm import Session

#local dependencies
from app.schema.document_schema import DocumentCreateClientRequest, DocumentCreatedClientResponse, DocumentGetByIdClientResponse
from app.repository import document_repository


async def get_by_id(id: int, db: Session) -> DocumentGetByIdClientResponse:
    '''
    service for getting a document by id number
    '''
    repository_response = await document_repository.get_by_id(id=id, db=db)

    return DocumentGetByIdClientResponse(
        id=repository_response.id,
        title=repository_response.title
    )


async def create_document(document_body: DocumentCreateClientRequest, db: Session) -> DocumentCreatedClientResponse:
    '''
    service for a creating document
    '''
    return await document_repository.create_document(document_body=document_body, db=db)