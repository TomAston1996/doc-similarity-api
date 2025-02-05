# ______ _____ _____       _____ ________  ___        ___  ______ _____
# |  _  \  _  /  __ \     /  ___|_   _|  \/  |       / _ \ | ___ \_   _|
# | | | | | | | /  \/_____\ `--.  | | | .  . |______/ /_\ \| |_/ / | |
# | | | | | | | |  |______|`--. \ | | | |\/| |______|  _  ||  __/  | |
# | |/ /\ \_/ / \__/\     /\__/ /_| |_| |  | |      | | | || |    _| |_
# |___/  \___/ \____/     \____/ \___/\_|  |_/      \_| |_/\_|    \___/

"""
App entry point
Author: Tom Aston
"""

from fastapi import FastAPI

from app.api.routes import routers
from app.core.config import config_manager


class AppCreator:
    """
    Application Context Creator
    """

    def __init__(self) -> None:
        self.app = FastAPI(
            title=config_manager.PROJECT_NAME, version=config_manager.VERSION
        )

        @self.app.get("/", tags=["root"])
        def root() -> str:
            return "server is running"

        self.app.include_router(routers)

def add(a, b):
    return a + b

app_creator = AppCreator()
app = app_creator.app
