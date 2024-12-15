'''
Document Schema
Author: Tom Aston
'''
#external dependencies
from pydantic import BaseModel

class DocumentBase(BaseModel):
    '''
    document schema
    '''
    title: str
    content: str