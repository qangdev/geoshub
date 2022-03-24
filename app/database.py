from sqlite3 import connect
from sqlalchemy import create_engine
from sqlalchemy import MetaData

from app.settings import Settings

settings = Settings()
metadata = MetaData()
engine = create_engine(settings.APP_DATABASE_URL)


def get_db():
    connection = None
    try:
        connection = engine.connect()
        yield connection
    finally:
        if connection is not None:
            connection.close()
