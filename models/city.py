#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'City'

    state_id = Column(String(60), nullable=False)
    name = Column(String(128), nullable=False, default="")
