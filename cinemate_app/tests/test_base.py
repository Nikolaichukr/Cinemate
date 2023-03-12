import unittest
from config import TestConfig
from cinemate_app import app, db


class Base(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            db.create_all()
        app.config.from_object(TestConfig)

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
