"""
Database Connection and Session Management
"""
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

DATABASE_PATH = config.DATABASE_PATH
DATABASE_URL = config.DATABASE_URL

Base = declarative_base()


@lru_cache(maxsize=8)
def get_engine(db_url=None):
    """Return a process-wide engine for the requested database URL."""
    url = db_url or DATABASE_URL
    return create_engine(url, echo=False)


@lru_cache(maxsize=8)
def _get_session_factory(db_url=None):
    """Return a cached session factory; sessions themselves are never shared."""
    return sessionmaker(bind=get_engine(db_url))


def get_session(db_url=None):
    """Create a new, independent database session."""
    return _get_session_factory(db_url)()


def init_db(db_url=None):
    """Initialize database with schema"""
    from . import Paper, Dataset, TrainingDataset, SFTMethod, RLMethod, FoundationModel
    
    engine = get_engine(db_url)
    Base.metadata.create_all(engine)
    print("Database initialized successfully")
