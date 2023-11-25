import pytest
from fastapi.testclient import TestClient
from url_shortener.app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from url_shortener.database import base, get_db
import settings


secrets = settings.get_settings()

SQLALCHEMY_DATABASE_URL = f"postgresql://{secrets.database_username}:{secrets.database_password}@" \
                          f"{secrets.database_hostname}/{secrets.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create a session
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    base.metadata.drop_all(bind=engine)
    base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():

        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
