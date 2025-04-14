# src/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI

# Create engine
engine = create_engine(DATABASE_URI, echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for models
Base = declarative_base()
