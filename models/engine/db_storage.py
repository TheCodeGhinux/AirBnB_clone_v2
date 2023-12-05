#!/usr/bin/python3
"""DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """Class that defines db storage engine.

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Represents and creates a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session
            queries all types of objects If cls is None.

        Return:
            Dict of classes like:
            key = <class name>.<obj id>
            value = object
        """
        new_obj = []
        if cls is None:
            classes_to_query = [State, City, User, Place, Review, Amenity]
            new_obj.extend(self.__session.query(*classes_to_query).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            new_obj.extend(self.__session.query(cls).all())
        return {"{}.{}".format(type(o).__name__, o.id): o for o in new_obj}

    def new(self, obj):
        """Add the object to the current database session"""
        if obj not in self.__session:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Close SQLAlchemy session."""
        self.__session.remove()
