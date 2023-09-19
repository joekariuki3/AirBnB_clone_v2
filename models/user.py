#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place

class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"
    password = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
