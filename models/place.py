#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ARRAY


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'Place'

    city_id = Column(String(128), nullable=False)
    user_id = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False, default="")
    description = Column(String(1024), nullable=True, default="")
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False, default=0.0)
    longitude = Column(Float, nullable=False, default=0.0)
    amenity_ids = Column(ARRAY(String(60)), nullable=True, default=[])
