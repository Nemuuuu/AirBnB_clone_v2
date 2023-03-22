## AirBnB_clone_2

Description
In this project we learned how to build a database engine with the SQLAlchemy Python library.


Classes

HBNB supports the following classes:

BaseModel
User
State
City
Amenity
Place
Review
Storage
The above classes are handled by one of either two abstracted storage engines, depending on the call - FileStorage or DBStorage.

FileStorage
The default mode.

In FileStorage mode, every time the backend is initialized, HBnB instantiates an instance of FileStorage called storage. The storage object is loaded/re-loaded from any class instances stored in the JSON file file.json. As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the file.json.

DBStorage
Run by setting the environmental variables HBNB_TYPE_STORAGE=db.

In DBStorage mode, every time the backend is initialized, HBNB instantiates an instance of DBStorage called storage. The storage object is loaded/re-loaded from the MySQL database specified in the environmental variable HBNB_MYSQL_DB, using the user HBNB_MYSQL_USER, password HBNB_MYSQL_PWD, and host HBNB_MYSQL_HOST. As class instances are created, updated, or deleted, the storage object is used to register changes in the corresponding MySQL database. Connection and querying is achieved using SQLAlchemy.

Testing
Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

$ python3 unittest -m discover tests
Alternatively, you can specify a single test file to run at a time:

$ python3 unittest -m tests/test_console.py
