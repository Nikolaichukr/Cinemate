import os
from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

MIGRATIONS_DIRECTORY = os.path.join("cinemate_app", "migrations")
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATIONS_DIRECTORY)

from .views import movies, reviews

app.register_blueprint(movies, url_prefix='/')
app.register_blueprint(reviews, url_prefix='/reviews')
