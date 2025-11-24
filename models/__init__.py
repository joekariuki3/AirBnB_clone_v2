#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage
or database storage depending on the environment variable
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from .engine import engine_config

if engine_config.storage_type == "db":
    """ uses database storage """
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
else:
    """ uses file storage """
    from models.engine.file_storage import FileStorage

    storage = FileStorage()

storage.reload()
