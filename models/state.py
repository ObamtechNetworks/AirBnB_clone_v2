#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    from models.city import City
    cities = relationship(
            'City',
            backref='state',
            cascade='all, delete, delete-orphan')

    # getter attribute for FileStorage
    @property
    def cities(self):
        from models.storage import storage
        city_instances = [
                city for city in storage.all('City').values()
                if city.state_id == self.id
                ]
        return city_instances
