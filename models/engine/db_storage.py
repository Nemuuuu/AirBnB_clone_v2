#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage:
	""" Database Storage class """
	__engine = None
	__session = None
	def __init__(self):

		# retrieving values via environment variables
		HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
		HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
		HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
		HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')

		# create engine
		self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
		
		# drop if env't == test
		if getenv('HBNB_ENV') == 'test':
			Base.metadata.drop_all(self.__engine)

	def all(self, cls=None):
		# query
		if cls == None:
			query = self.__session.query(State).all()
			query.extend(self.__session.query(City).all())
			query.extend(self.__session.query(User).all())
			query.extend(self.__session.query(Place).all())
			query.extend(self.__session.query(Review).all())
			query.extend(self.__session.query(Amenity).all())
			
		# returns dictionary
		return {
				 "{}.{}".format(type(obj).__name__, obj.id):
				 obj for obj in query
				}

	def new(self, obj):
		"""add object to current database session"""
		self.__session.add(obj)

	def save(self):
		"""commit changes of current database session"""
		self.__session.commit()

	def delete(self, obj=None):
		""" delete from current database session if obj is not 'None' """
		if obj != None:
			self.__session.delete(obj)

	def reload(self):
		""" reload from the database """

		# create all tables inthe DB
		Base.metadata.create_all(self.__engine)
		
		# create current database session fro engine
		Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
		self.__session = Session()
