"""
This module contains the configuration settings for a web application.
It loads environment variables from a .env file using the dotenv and os modules.
The Config class sets the configuration settings for the application,
including the database URI and the application's secret key.
"""
import os
from dotenv import load_dotenv

load_dotenv()
user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
server = os.environ.get('MYSQL_SERVER')
database = os.environ.get('MYSQL_DATABASE')


# pylint: disable=too-few-public-methods
class Config:
    """This class sets the configuration settings for a web application"""
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{user}:{password}@{server}/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    """This class sets configuration settings for testing"""
    TESTING = True
    WTF_CSRF_ENABLED = False
