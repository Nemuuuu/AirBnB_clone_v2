#!/usr/bin/python3
""" State Module for HBNB project """
from base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv 

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db': # DB storage
        cities = relationship('City', backref='state', cascase='all, delete')
    else: # file storage
        @property
        def cities(self):
            """ getter attribute that returns list of City """
            from models import storage
            from models.city import City
            city_lists = []
            city = storage.all(City)
            for c in city.values():
                if c.stated_id == self.id:
                    city_lists.append(c)
            return city_lists
