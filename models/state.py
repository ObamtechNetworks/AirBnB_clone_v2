#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # run this only when it's the db storage
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        from models.city import City
        cities = relationship(
                'City',
                backref='state',
                cascade='all, delete, delete-orphan')
    else:
        # getter attribute for FileStorage
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes the state model """
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Getter for cities """
            from models.storage import storage
            city_instances = [
                    city for city in storage.all('City').values()
                    if city.state_id == self.id]
            return city_instances
