#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.user import User
from models.document import Document
from models.text_block import TextBlock
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# import psycopg2
import pymysql

classes = {"User": User,
           "Document": Document,
           "TextBlock": TextBlock}


class DBStorage:
    """interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        USER = getenv('USER')
        PASSWORD = getenv('PASSWORD')
        HOST = getenv('HOST')
        DB = getenv('DB')
        # self.__engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.
        #                               format(USER,
        #                                      PASSWORD,
        #                                      HOST,
        #                                      DB))
        self.__engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.
                                      format(USER,
                                             PASSWORD,
                                             HOST,
                                             DB))

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None
        return self.__session.query(cls).filter(cls.id == id).first()

    def get_by(self, cls, key, value):
        """
        Returns the object based on the class name and its keys and values, or
        None if not found
        """
        if cls not in classes.values():
            return None
        return self.__session.query(cls) \
            .filter(getattr(cls, key) == value).all()

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        if cls:
            return len(models.storage.all(cls).values())
        else:
            count = 0
            for clas in classes.values():
                count += len(models.storage.all(clas).values())
            return count
