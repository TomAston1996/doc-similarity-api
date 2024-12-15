#______ _____ _____       _____ ________  ___        ___  ______ _____ 
#|  _  \  _  /  __ \     /  ___|_   _|  \/  |       / _ \ | ___ \_   _|
#| | | | | | | /  \/_____\ `--.  | | | .  . |______/ /_\ \| |_/ / | |  
#| | | | | | | |  |______|`--. \ | | | |\/| |______|  _  ||  __/  | |  
#| |/ /\ \_/ / \__/\     /\__/ /_| |_| |  | |      | | | || |    _| |_ 
#|___/  \___/ \____/     \____/ \___/\_|  |_/      \_| |_/\_|    \___/

'''
Main
Author: Tom Aston
'''
#external dependencies
from fastapi import FastAPI

#local dependencies
from app.api.routes import routers
from app.core.config import config_manager


class AppCreator:
    '''
    Application Context Creator
    '''
    def __init__(self) -> None:
        self.app = FastAPI(
            title=config_manager.PROJECT_NAME,
            version=config_manager.VERSION
        )

        #set routes
        @self.app.get('/')
        def root() -> str:
            return 'server is running'

        self.app.include_router(routers)

app_creator = AppCreator()
app = app_creator.app
        
