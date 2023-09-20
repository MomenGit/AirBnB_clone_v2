#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenities import Amenity

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', back_populates='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False,
            back_populates='place_amenities')
    else:
        @property
        def reviews(self):
            """
            eturns the list of Review instances
            with place_id equals to the current Place.id
            It will be the FileStorage relationship
            between Place and Review
            """
            from models import storage
            list_reviews = list()
            for obj in storage.all(Review).values():
                if obj.place_id == self.id:
                    list_reviews.append(obj)
            return (list_reviews)
