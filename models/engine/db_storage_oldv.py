#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import models
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """
    DBStorage Class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        initialization
        """
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
                username, password, host, db_name)

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query and return all
        """
        objs_list = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                objs_list = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                objs_list.extend(self.__session.query(subclass).all())

        obj_dict = {}
        for obj in objs_list:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """
        add object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete an element in the table
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
