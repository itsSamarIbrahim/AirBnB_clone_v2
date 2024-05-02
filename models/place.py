#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
import models
from models.review import Review
from sqlalchemy import (Column, String, ForeignKey,
                        Float, Integer, Table)
from sqlalchemy.orm import relationship

assertion_table = Table('place_amenity', Base.metadata,
                        Column('place_id', String(60),
                        ForeignKey('places.id'), primary_key=True,
                        nullable=False),
                        Column('amenity_id', String(60), ForeignKey('amenities.id'),
                               primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place', cascade='all, delete-orphan')
    amenities = relationship('Amenity', secondary='place_amenity',
                             viewonly=False, overlaps="place_amenities")
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """
            
            """
            all_reviews = list(models.storage.all(Review).values())
            review_list = [rev for rev in all_reviews if rev.place_id == self.id]

            return review_list
        @property
        def amenities(self):
            """
            
            """
            all_amenities = list(models.storage.all(Amenity).values())
            amenty_list = [a for a in all_amenities if a.id in self.amenity_ids]
            return amenty_list

        @amenities.setter
        def amenities(self, value):
            """
            
            """
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)