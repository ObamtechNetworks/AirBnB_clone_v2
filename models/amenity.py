#!/usr/bin/python3
""" Amenities Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.place import Place


class Amenity(BaseModel, Base):
    """ models for all amenities """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    # establish a many to many relationship
    place_amenities = relationship('Place',
                                   secondary='place_amenity',
                                   backref='places_amenities',
                                   overlaps="amenities")
