"""
Connecting to DB with SQLAlchemy ORM
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from sqlalchemy.exc import SQLAlchemyError
import os
import logging

# Connect to the DB
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL, echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# Get a session per request to transact against DB
def get_db_session():
    session = Session()
    try:
        yield session
        session.commit()
    except SQLAlchemyError as e:
        logging.error(f"Database error occurred: {e}")
        session.rollback()
        raise
    finally:
        session.close()
