#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from hashlib import md5
import re


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

    def is_valid_password(self, pwd):
        """validates a password"""
        return md5(pwd.encode()).hexdigest() == self.password

    @classmethod
    def is_valid_email(email):
        """validates an email address"""
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_regex, email) is not None
