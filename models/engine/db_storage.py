#!/usr/bin/python3
"""Module defines DBStorage which is used by HBNB clone to interact with DB"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages data storage in a MySQL DB"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage engine instance"""
        from models.base_model import Base
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        uri = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db_name)
        self.__engine = create_engine(uri, pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects in the database"""
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {'Amenity': Amenity, 'City': City, 'Place': Place,
                   'Review': Review, 'State': State, 'User': User}
        output = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.to_dict()['__class__'] + '.' + obj.id
                output[key] = obj
        else:
            for cls in classes.keys():
                objs = self.__session.query(classes[cls]).all()
                for obj in objs:
                    key = obj.to_dict()['__class__'] + '.' + obj.id
                    output[key] = obj
        return output

    def new(self, obj):
        """Adds the object to the current DB session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes in the session to the DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes specified object from current DB session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all the tables in the database and creates a new DB session
        """
        from models.amenity import Amenity
        from models.base_model import Base
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Closes the current DBStorage session """
        self.__session.close()
