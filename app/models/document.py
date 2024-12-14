from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.sql import func

from app.core.database import Base

class Document(Base):
    '''
    docuement database model
    '''
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=False)
    created = Column(TIMESTAMP, server_default=func.now())