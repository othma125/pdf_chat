#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import urllib.parse


class Document(BaseModel, Base):
    """Document class """
    __tablename__ = 'documents'
    UserID = Column(String(60), ForeignKey('users.id'))
    FileName = Column(String(255), nullable=False)
    URL = Column(String(255), nullable=False)
    Status = Column(String(10), default="uploaded") #Status (e.g., "uploaded", "processed", "indexed")
    TextBlocks = relationship("TextBlock",
                                   backref="document",
                                   cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes document"""
        super().__init__(*args, **kwargs)
    

    def __init__(self, *args, **kwargs):
        """initializes document"""
        super().__init__(*args, **kwargs)
    
    @classmethod
    def is_valid_url(cls, url):
        try:
            result = urllib.parse.urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
