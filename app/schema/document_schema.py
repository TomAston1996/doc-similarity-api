'''
Document Schema
Author: Tom Aston
'''
#external dependencies
from pydantic import BaseModel

class DocumentBase(BaseModel):
    '''
    @brief document schema
    @feild title: str
    @feild content: str
    '''
    title: str
    content: str