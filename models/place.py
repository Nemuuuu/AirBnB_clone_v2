#!/usr/bin/python3
""" Place Module for HBNB project """
from base_model import BaseModel, Base
from sqlalchemy import Column, Integer,Table, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table(
            'place_amenity', # table name
            Base.metadata, # metadata
            Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
        )
class Place(BaseModel, Base):
    """ A place to stay """
    
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # update place for DB and file storages
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref= 'place', cascade='all, delete')
        amenities = relationship('Amenity', secondary='place_amenity', viewonly=False, backref='places')
    else:
        @property
        def reviews(self):
            """ getter attribute that returns list of Review instances """
            from models import storage
            from models.review import Review
            review_lists = []
            review = storage.all(Review)
            for r in review.values():
                if r.place_id == self.id:
                    review_lists.append(r)
            return review_lists
        
        @property
        def amenities(self):
            """ getter attribute that returns the list of Amenity instances """
            from models import storage
            from models.amenity import Amenity
            amenity_lists = []
            amenity = storage.all(Amenity)
            for a in amenity.values():
                if a.amenity_ids == self.id:
                    amenity_lists.append(a)
            return amenity_lists
        
        @amenities.setter
        def amenities(self, obj=None):
            """ setter attribute for amenities """
            from models.amenity import Amenity
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
