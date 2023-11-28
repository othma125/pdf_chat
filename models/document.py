#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Document(BaseModel, Base):
    """Document class """
    __tablename__ = 'documents'
    UserID = Column(String(60), ForeignKey('users.id'))
    FileName = Column(String(255))
    Status = Column(String(10)) #Status (e.g., "uploaded", "processed", "indexed")

    def __init__(self, *args, **kwargs):
        """initializes document"""
        super().__init__(*args, **kwargs)
    

    def __init__(self, *args, **kwargs):
        """initializes document"""
        super().__init__(*args, **kwargs)
