from fastapi import APIRouter, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session

from app.models import document
from app.schema import document_schema
from app.core.database import SessionLocal

router = APIRouter(
    prefix='/document',
    tags=['document']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get('/{id}')
async def get(id: int, db: db_dependency):
    '''
    GET a document by id number
    '''
    result = db.query(document.Document).filter(document.Document.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail='document id not found')
    return result

@router.post('')
async def post(document_body: document_schema.DocumentBase, db: db_dependency):
    '''
    CREATE a new document
    '''
    db_document = document.Document(title=document_body.title, content=document_body.content)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)