#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place
from .engine import engine_config


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"

    if engine_config.storage_type == "db":
        """ uses database storage """
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", cascade="all, delete", backref="user")
        reviews = relationship("Review", cascade="all, delete", backref="user")
    else:
        """ uses file storage """
        email = ""
        password = ""
        first_name = ""
        last_name = ""
