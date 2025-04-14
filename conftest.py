# tests/conftest.py
import sys
import os
import pytest
from src.db.database import engine, Session, Base
from src.services.user_service import create_user

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def setup_test_data(db_session):
    create_user(db_session, "Test User", "test@example.com")
    return db_session
