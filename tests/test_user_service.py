# tests/test_user_service.py
from src.services.user_service import create_user

def test_create_user(db_session):
    # Arrange
    name = "John Doe"
    email = "john@example.com"

    # Act
    user = create_user(db_session, name, email)

    # Assert
    assert user.name == name
    assert user.email == email



def test_create_duplicate_user(db_session):
    email = "john@example.com"
    create_user(db_session, "John Doe", email)
    try:
        create_user(db_session, "John Doe", email)
        assert False, "Should raise an error for duplicate email"
    except Exception:
        assert True