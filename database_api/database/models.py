"""
Database models for SnipShot Database API (Supabase Edition)

User management is handled by Supabase Auth.
We only store image metadata here.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Image(Base):
    """
    Image metadata model.
    
    user_id is the Supabase Auth user UUID (string, not integer).
    Actual image files are stored in Supabase Storage.
    """
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(36), nullable=False, index=True)  # Supabase UUID
    
    # Supabase Storage info
    storage_path = Column(Text, nullable=False)  # Path in Supabase Storage
    public_url = Column(Text, nullable=False)    # Public URL for the image
    
    # Metadata
    original_filename = Column(String(255), nullable=True)
    source_language = Column(String(10), nullable=True)
    target_language = Column(String(10), nullable=True)
    file_size = Column(Integer, nullable=True)  # Size in bytes
    
    created_at = Column(DateTime, default=datetime.utcnow)
