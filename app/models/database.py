"""
Database Connection and Session Management
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

DATABASE_PATH = config.DATABASE_PATH
DATABASE_URL = config.DATABASE_URL

Base = declarative_base()


def get_engine(db_url=None):
    """Create and return database engine"""
    url = db_url or DATABASE_URL
    return create_engine(url, echo=False)


def get_session(db_url=None):
    """Create and return database session"""
    engine = get_engine(db_url)
    Session = sessionmaker(bind=engine)
    return Session()


def init_db(db_url=None):
    """Initialize database with schema"""
    from . import Paper, Dataset, TrainingDataset, SFTMethod, RLMethod, FoundationModel
    
    engine = get_engine(db_url)
    Base.metadata.create_all(engine)
    print("Database initialized successfully")
