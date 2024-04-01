#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    # define instance of the association table for many-to-many relnshp
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id',
                                            ondelete='CASCADE'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id',
                                            ondelete='CASCADE'),
                                 primary_key=True, nullable=False))

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete, delete-orphan')

        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=False,
                                 overlaps="amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Getter for reviews"""
            from models import storage
            review_instances = model.storage.all("Review").values()
            review_list = []
            for reveiw in review_instances:
                if reveiw.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Getter for amenities"""
            return [
                    amenity for amenity in
                    models.storage.all(Amenity) if
                    amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """setter attribute amenities"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
