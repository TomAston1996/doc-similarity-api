'''
Document Schema
Author: Tom Aston
'''

#inbuild dependencies
from datetime import datetime

#external dependencies
from pydantic import BaseModel


class DocumentCreateClientRequest(BaseModel):
    '''
    client request body for creating a new document
    '''
    title: str
    content: str


class DocumentCreatedClientResponse(BaseModel):
    '''
    client reponse for creating a new document
    '''
    id: int
    title: str
    content: str
    created: datetime


class DocumentGetByIdClientResponse(BaseModel):
    '''
    client reponse for getting a document by id
    '''
    id: int
    title: str
