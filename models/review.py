#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv

class Review(BaseModel):
    """ Review classto store review information """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
        user_id = Column(String(60), nullable=False, ForeignKey('places.id'))
    
    else:    
        place_id = ""
        user_id = ""
        text = ""
