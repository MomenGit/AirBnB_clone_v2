#!/usr/bin/python3
""""""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os


class DBStorage():
    """"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

    def all(self, cls=None):
        pass

    def new(self, obj):
        pass

    def save(self):
        pass

    def delete(self, obj=None):
        pass

    def reload(self):
        pass
