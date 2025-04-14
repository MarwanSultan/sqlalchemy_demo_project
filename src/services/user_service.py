# src/services/user_service.py
from sqlalchemy.orm import Session
from src.models.users import User
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_user(db: Session, name: str, email: str):
    logger.info(f"Creating user: {email}")
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
