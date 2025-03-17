import importlib
from config import settings


class Config:
    def __init__(self):
        self.appname = settings.APP_NAME
        self.appversion = settings.APP_VERSION
        self.debug = settings.DEBUG
        self.db_url = settings.DB_URL


g = Config()
