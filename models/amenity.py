#!/usr/bin/python3
""" State Module for HBNB project """
from base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from place import Place, place_amenity

class Amenity(BaseModel, Base):
    """ Amenity class """

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    # represent many-to-many relationship between class Place and Amenity
    place_amenities = relationship('Place', secondary=place_amenity)
