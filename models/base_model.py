#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from os import getenv
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


if getenv("HBNB_TYPE_STORAGE") == 'db':
    # create the Base object
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        # create the required class attributes
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(
                DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(
                DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs or type(self.created_at) is str:
                self.created_at = datetime.utcnow()
            if 'updated_at' not in kwargs or type(self.updated_at) is str:
                self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """ To delete the current instance from the storage
        (models.storage) by calling the delete
        """
        from models.storage import storage
        # delete an instance by calling the delete method
        storage.delete(self)
