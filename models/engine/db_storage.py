#!/usr/bin/python3
""""""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class DBStorage():
    """"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        self.__engine = create_engine()

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
