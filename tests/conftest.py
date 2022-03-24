# pylint: disable=redefined-outer-name
import time
from pathlib import Path

import pytest

from sqlalchemy import create_engine
from fastapi.testclient import TestClient

from app.application import app
from app.database import metadata, get_db


def _get_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def db(in_memory_db):
    connection = in_memory_db.connect()
    try:
        yield connection
    finally:
        connection.close()


@pytest.fixture
def client() -> TestClient:
    # app.settings.APP_DATABASE_URL = "sqlite:///:memory:"
    app.dependency_overrides[get_db] = _get_db
    yield TestClient(app)
