'''
Document Model
Author: Tom Aston
'''

#external dependencies
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.sql import func

#local dependencies
from app.core.database import BaseModel

class Document(BaseModel):
    '''
    document database model
    '''
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=False)
    created = Column(TIMESTAMP, server_default=func.now())