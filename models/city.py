#!/usr/bin/python3
"""City Module for HBNB project"""

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .engine import engine_config


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"

    if engine_config.storage_type == "db":
        """ use database storage """
        name = Column("name", String(128), nullable=False)
        state_id = Column(
            "state_id", String(60), ForeignKey("states.id"), nullable=False
        )
        places = relationship(
            "Place", cascade="all, delete, delete-orphan", backref="cities"
        )
    else:
        """ use file storage """
        state_id = ""
        name = ""
