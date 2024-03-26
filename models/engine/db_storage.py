#!/usr/bin/python3
"""A new engine that interacts with the given database"""

import os
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

cls_models = {
        'User': User,
        'State': State,
        'City': City,
        'Review': Review,
        'Place': Place
        # 'Amenity': Amenity,
        }


class DBStorage:
    """ class that setup the dbstorage engine """

    __engine = None
    __session = None

    def __init__(self):
        """ instance intialziation """
        # retrieve environment variable
        sql_user = os.getenv('HBNB_MYSQL_USER')
        sql_pwd = os.getenv('HBNB_MYSQL_PWD')
        sql_host = 'localhost'
        sql_db = os.getenv('HBNB_MYSQL_DB')

        # setup connection URL
        db_type = "mysql+mysqldb"
        URL = "{}://{}:{}@{}:3306/{}".format(
                db_type,
                sql_user,
                sql_pwd,
                sql_host,
                sql_db)

        self.__engine = create_engine(URL, pool_pre_ping=True)

        # if test environmnet drop tables
        if os.getenv('HBNB_ENV') == 'test':
            # drop tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session
        query all objs based on the class name
        Return:
            A dictionary with the format key:
            <class-name>.<object-id>, value = object
        """
        # investigate what this is for
        if not self.__session:
            self.reload()

        objects = {}

        if type(cls) == str:
            cls = cls_models.get(cls, None)
        if cls:
            for obj in self.__session.query(cls).all():
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            # quer all objects from all classes
            for cls in cls_models.values():
                for obj in self.__session.query(cls).all():
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj
        return objects

    def new(self, obj):
        """ Adds the object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ if called, if obj is not None,
        delete that object from the current database session
        """
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ creates all tables in the database """
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def __del__(self):
        """ close the session when the object is destroyed """
        self.__session.close()
    
    def close(self):
        """calls remove method to remove session"""
        self.__session.remove()
