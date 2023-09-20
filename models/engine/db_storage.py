#!/usr/bin/python3
""""""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage():
    """"""
    __engine = None
    __session = None

    def __init__(self) -> None:

        if (getenv('HBNB_ENV') == 'test'):
            pass

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            cls_objects = {}
            for key, val in self.__session.query(cls).all():
                if cls == val.__class__:
                    cls_objects[key] = val
            return cls_objects

    def new(self, obj):
        """"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        pass

    def delete(self, obj=None):
        pass

    def reload(self):
        from models.base_model import Base
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
