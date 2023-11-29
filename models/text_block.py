#!/usr/bin/python
""" holds class TextBlock"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class TextBlock(BaseModel, Base):
    """Representation of a text block """
    __tablename__ = 'text_blocks'
    DocumentID = Column(String(60), ForeignKey('documents.id'))
    TextContent = Column(String(255), nullable=False)
    PageNumber = Column(Integer)
    

    def __init__(self, *args, **kwargs):
        """initializes text block"""
        super().__init__(*args, **kwargs)

