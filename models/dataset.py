"""
Dataset Models
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Index
from .database import Base


class Dataset(Base):
    __tablename__ = 'datasets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    language = Column(String)
    multimodal = Column(String)
    repos = Column(String)
    amount = Column(String)
    environment = Column(String)
    category = Column(String)
    github_link = Column(String)
    huggingface_link = Column(String)
    website_link = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'language': self.language,
            'multimodal': self.multimodal,
            'repos': self.repos,
            'amount': self.amount,
            'environment': self.environment,
            'category': self.category,
            'links': {
                'github': self.github_link,
                'huggingface': self.huggingface_link,
                'website': self.website_link
            },
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class TrainingDataset(Base):
    __tablename__ = 'training_datasets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    language = Column(String)
    repos = Column(String)
    amount = Column(String)
    github_link = Column(String)
    huggingface_link = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'language': self.language,
            'repos': self.repos,
            'amount': self.amount,
            'links': {
                'github': self.github_link,
                'huggingface': self.huggingface_link
            },
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


# Create indexes
Index('idx_datasets_language', Dataset.language)
