#!/usr/bin/python3
""" Amenity Module for HBNB project """

from models.base_model import BaseModel, Base
from models.place import Place, place_amenity
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    '''
    amenity class declaration
    can use file storage database storage
    '''

    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        '''
        use database storage
        '''
        name = Column('name', String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity,
                                       backref='amenities')
    else:
        '''
        use file storage
        '''
        name = ""
