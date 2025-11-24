from dotenv import load_dotenv
import os

load_dotenv()

HBNB_ENV = os.getenv("HBNB_ENV", "dev")
HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST", "localhost")
HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")
HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE", "file")


class EngineConfig:
    """
    This class contains the configuration for the engine
    """

    storage_type = HBNB_TYPE_STORAGE
    database_user = HBNB_MYSQL_USER
    database_password = HBNB_MYSQL_PWD
    database_host = HBNB_MYSQL_HOST
    database_name = HBNB_MYSQL_DB
    environment = HBNB_ENV


engine_config = EngineConfig()
