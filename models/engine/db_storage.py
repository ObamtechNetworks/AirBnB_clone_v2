#!/usr/bin/python3
"""A new engine that interacts with the given database"""

import os
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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
        sql_db  = os.getenv('HBNB_MYSQL_DB')

        # setup connection URL
        db_type = "mysql+mysqldb"
        URL = "{}://{}:{}@{}:3306/{}".format(
                db_type,
                sql_user,
                sql_pwd,
                sql_host,
                sql_db)

        # create engine
        print("creating engine...")
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
        result = {}
        classes = [cls] if cls else [
                User,
                State,
                City,
                Amenity,
                Place,
                Review]
        for class_to_query in classes:
            # retrieve all objects based on the given class
            objects = self.__session.query(class_to_query).all()
            print(objects)  # debugging
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                result[key] = obj
        return result

    def new(self, obj):
        """ Adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ if called, if obj is not None,
        delete that object from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ creates all tables in the database """
        print("creating tables")
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
                sessionmaker(
                    bind=self.__engine,
                    expire_on_commit=False))
    def __del__(self):
        """ close the session when the object is destroyed """
        self.__session.close()
