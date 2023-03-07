"""
This file is used to initialize all modules.
"""
import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import Config

MIGRATIONS_DIRECTORY = os.path.join("cinemate_app", "migrations")
LOG_FILE_PATH = "cinemate.log"

# App and configuration
app = Flask(__name__)
app.config.from_object(Config)

# Logging
# Logging to file
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
file_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=1024 * 1024 * 10, backupCount=10)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# Logging on the console
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# Logging from werkzeug
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.handlers.clear()
werkzeug_logger.addHandler(file_handler)
werkzeug_logger.addHandler(console_handler)
werkzeug_logger.setLevel(logging.DEBUG)

# Setting up app logger with corresponding handlers
# pylint: disable=no-member
logger = app.logger
logger.handlers.clear()
app.logger.addHandler(file_handler)
app.logger.addHandler(console_handler)
app.logger.setLevel(logging.DEBUG)
logger.info('Cinemate app starting...')

# Database
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATIONS_DIRECTORY)

# RESTful API
# It's necessary to import some modules here to avoid circular import
# pylint: disable=wrong-import-position
from .rest import movie_api, review_api

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

api.add_resource(movie_api.MovieList, '/movies')
api.add_resource(movie_api.Movie, '/movie/<int:movie_id>')
api.add_resource(review_api.ReviewList, '/reviews')
api.add_resource(review_api.Review, '/review/<int:review_id>')

from .views import movies, reviews

app.register_blueprint(movies, url_prefix='/')
app.register_blueprint(reviews, url_prefix='/reviews')
app.register_blueprint(api_blueprint, url_prefix='/api')
