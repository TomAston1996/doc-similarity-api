'''
Document Repository Layer
Author: Tom Aston
'''

#external dependencies
from fastapi import HTTPException
from sqlalchemy.orm import Session

#local dependencies
from app.models.document import Document
from app.core.database import database
from app.schema.document_schema import DocumentCreateClientRequest, DocumentCreatedClientResponse


async def get_by_id(id: int, db: Session):
    '''
    GET a document by id number
    '''
    result = db.query(Document).filter(Document.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail='document id not found')
    return result


async def create_document(document_body: DocumentCreateClientRequest, db: Session) -> DocumentCreatedClientResponse:
    '''
    CREATE a new document
    '''
    db_document = Document(title=document_body.title, content=document_body.content)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    return DocumentCreatedClientResponse(
        id=db_document.id,
        title=db_document.title,
        content=db_document.content,
        created=db_document.created
    )