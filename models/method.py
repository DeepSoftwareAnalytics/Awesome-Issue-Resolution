"""
Method Models (SFT, RL, Foundation)
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Index
from .database import Base


class SFTMethod(Base):
    __tablename__ = 'sft_methods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String, unique=True, nullable=False)
    base_model = Column(String)
    size = Column(String)
    architecture = Column(String)
    training_scaffold = Column(String)
    resolution_percent = Column(Float)
    code_link = Column(String)
    data_link = Column(String)
    model_link = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'model_name': self.model_name,
            'base_model': self.base_model,
            'size': self.size,
            'architecture': self.architecture,
            'training_scaffold': self.training_scaffold,
            'resolution_percent': self.resolution_percent,
            'links': {
                'code': self.code_link,
                'data': self.data_link,
                'model': self.model_link
            },
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class RLMethod(Base):
    __tablename__ = 'rl_methods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String, unique=True, nullable=False)
    base_model = Column(String)
    size = Column(String)
    architecture = Column(String)
    training_scaffold = Column(String)
    reward_type = Column(String)
    resolution_percent = Column(Float)
    code_link = Column(String)
    data_link = Column(String)
    model_link = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'model_name': self.model_name,
            'base_model': self.base_model,
            'size': self.size,
            'architecture': self.architecture,
            'training_scaffold': self.training_scaffold,
            'reward_type': self.reward_type,
            'resolution_percent': self.resolution_percent,
            'links': {
                'code': self.code_link,
                'data': self.data_link,
                'model': self.model_link
            },
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class FoundationModel(Base):
    __tablename__ = 'foundation_models'

    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String, unique=True, nullable=False)
    size = Column(String)
    architecture = Column(String)
    inference_scaffold = Column(String)
    reward_type = Column(String)
    resolution_percent = Column(Float)
    code_link = Column(String)
    model_link = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'model_name': self.model_name,
            'size': self.size,
            'architecture': self.architecture,
            'inference_scaffold': self.inference_scaffold,
            'reward_type': self.reward_type,
            'resolution_percent': self.resolution_percent,
            'links': {
                'code': self.code_link,
                'model': self.model_link
            },
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


# Create indexes
Index('idx_sft_methods_resolution', SFTMethod.resolution_percent)
Index('idx_rl_methods_resolution', RLMethod.resolution_percent)
Index('idx_foundation_models_resolution', FoundationModel.resolution_percent)
