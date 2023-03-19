#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    # class attribute places, reviews represent a relationship with the class 'Place' and 'Review' respectively. If the User object is deleted, all linked Place and Review objects must be automatically deleted. Also, the reference from a Place and Review object to his User should be named user
    places = relationship('Place', backref = 'user', cascade = 'all, delete')
    reviews = relationship('Review', backref = 'user', cascade = 'all, delete')