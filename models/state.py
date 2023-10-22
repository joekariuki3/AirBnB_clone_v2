#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        """ use database storage """
        name = Column('name', String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        """ use file storage """
        name = ''

    @property
    def cities(self):
        """
        return the list of city instance
        with state_id equal to current state
        """
        cities = list()
        for id, city in models.storage.all(City).items():
            if city.state_id == self.id:
                cities.append(city)
        return cities
