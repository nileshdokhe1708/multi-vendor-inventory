import pytest

from app.core.database import Base
from app.core.database import engine


from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(scope="function")
def reset_database():

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    yield