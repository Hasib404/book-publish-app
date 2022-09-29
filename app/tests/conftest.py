import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.base_class import Base
from db.session import get_db
from main import app


SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:5440/book-app-test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


@pytest.fixture
def db():
    yield TestingSessionLocal()
    for table in reversed(Base.metadata.sorted_tables):
        engine.execute(table.delete())


@pytest.fixture
def client(db):
    def test_db():
        return db

    app.dependency_overrides[get_db] = test_db
    return TestClient(app)
