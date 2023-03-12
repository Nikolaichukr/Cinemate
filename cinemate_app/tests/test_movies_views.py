from cinemate_app import app
from cinemate_app.service import populate_database
from cinemate_app.tests.test_base import Base


class MovieTest(Base):
    """
    Class for movie views test cases
    """

    def test_movies(self):
        """
        Test / views with and without entries in DB
        """
        tester = app.test_client()
        response = tester.get('/', content_type='html/text')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        populate_database.populate_with_dummy_data()
        tester = app.test_client()
        response = tester.get('/', content_type='html/text')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_movie(self):
        """
        Test /movie/<int:movie_id> views with get method
        """
        # if movie doesn't exist
        tester = app.test_client()
        response = tester.get('/movie/0')
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)

        # if movie exists
        tester = app.test_client()
        populate_database.populate_with_dummy_data()
        response = tester.get('/movie/1')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_add_movie(self):
        """
        Test /add_movie view with get and post methods
        """
        tester = app.test_client()
        response = tester.get('/add_movie', content_type='html/text')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        tester = app.test_client()
        response = tester.post('/add_movie', data={
            'title': 'TestTitle',
            'year': 2022,
            'director': 'TestDirector',
            'genre': 'TestGenre'
        }, follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_update_movie(self):
        """
        Test /update_movie/<int:movie_id> views with get and post
        methods, providing correct and incorrect information.
        """
        # if movie doesn't exist
        tester = app.test_client()
        response = tester.get('/update_movie/0')
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)

        # if movie exists
        tester = app.test_client()
        populate_database.populate_with_dummy_data()
        response = tester.get('/update_movie/1')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # if update movie
        tester = app.test_client()
        response = tester.post('/update_movie/1', data={
            'title': 'NewTitle',
            'year': 2023,
            'director': 'NewDirector',
            'genre': 'NewGenre'
        }, follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_delete_movie(self):
        """
        Test /delete_movie/<int:movie_id> views with get method.
        """
        # if movie doesn't exist
        tester = app.test_client()
        response = tester.get('/delete_movie/0')
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)
        # if movie exists
        populate_database.populate_with_dummy_data()
        tester = app.test_client()
        response = tester.get('/delete_movie/1',
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
