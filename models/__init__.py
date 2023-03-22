#!/usr/bin/python3
"""This module instantiates a storage object"""
import os
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


store_type = os.getenv('HBNB_TYPE_STORAGE')

if store_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()

# Enables us perform wildcard package importation
__all__ = ['Amenity', 'City', 'State', 'Place', 'Review', 'User', 'storage']
