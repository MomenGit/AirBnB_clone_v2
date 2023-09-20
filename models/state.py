#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City 


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            'City', cascade='all, delete, delete-orphan', back_populates='state')
    else:
        @property
        def cities(self):
            """
            returns the list of City instances
            with state_id equals to the current State.id
            It will be the FileStorage relationship
            between State and City
            """
            from models import storage
            list_cities = list()
            for obj in storage.all(City).values():
                if obj.state_id == self.id:
                    list_cities.append(obj)
            return (list_cities)
