"""
Paper Model
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Index
from .database import Base


class Paper(Base):
    __tablename__ = 'papers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_name = Column(String, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    authors = Column(Text, nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(String)  # Format: YYYY-MM
    venue = Column(Text, nullable=False)
    category = Column(String, nullable=False)  # Can be comma-separated
    abstract = Column(Text)
    arxiv_link = Column(String)
    github_link = Column(String)
    huggingface_link = Column(String)
    website_link = Column(String)
    doi_link = Column(String)
    openreview_link = Column(String)
    featured = Column(Boolean, default=False)  # Pinned to "Recent Papers" section
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'short_name': self.short_name,
            'title': self.title,
            'authors': self.authors,
            'year': self.year,
            'month': self.month,
            'venue': self.venue,
            'category': self.category,
            'abstract': self.abstract,
            'featured': bool(self.featured),
            'links': {
                'arxiv': self.arxiv_link,
                'github': self.github_link,
                'huggingface': self.huggingface_link,
                'website': self.website_link,
                'doi': self.doi_link,
                'openreview': self.openreview_link
            },
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


# Create indexes
Index('idx_papers_year', Paper.year)
Index('idx_papers_category', Paper.category)
