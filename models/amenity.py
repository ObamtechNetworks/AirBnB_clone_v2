#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String


class Amenity(BaseModel):
    """ models for all amenities """
    __tablename__ = 'Amenity'

    name = Column(String(128), nullable=False, default="")
