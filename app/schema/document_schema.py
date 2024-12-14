from pydantic import BaseModel

class DocumentBase(BaseModel):
    '''
    document schema
    '''
    title: str
    content: str