from fastapi import FastAPI

from app.api.routes import routers
from app.core.database import engine, Base

app = FastAPI()

#create all the database tables defined in models if they don't already exist
Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return 'server is running'

app.include_router(routers)
