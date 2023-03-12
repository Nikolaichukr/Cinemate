import json
from cinemate_app import app
from cinemate_app.service import populate_database, movie_service
from cinemate_app.tests.test_base import Base


class MoviesAPITest(Base):
    """
    Class for movie rest API test cases
    """

    def test_get_movies(self):
        """
        Test if /api/movies is working
        """
        tester = app.test_client()
        response = tester.get('/api/movies', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_movies_content_type(self):
        """
        Test if /api/movies return correct content type
        """
        tester = app.test_client()
        response = tester.get('/api/movies', follow_redirects=True)
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    def test_get_movies_data(self):
        """
        Test for correct content in response
        """
        populate_database.populate_with_dummy_data()
        tester = app.test_client()
        response = tester.get('/api/movies', follow_redirects=True)
        with app.app_context():
            movie = movie_service.get_movie_by_id(1)
        self.assertTrue(movie.title.encode() in response.data)

    def test_get_movie(self):
        """
        Test if /api/movie/<int:movie_id> is working
        """
        populate_database.populate_with_dummy_data()
        tester = app.test_client()
        response = tester.get('/api/movie/1', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_movie_content_type(self):
        """
        Test if /api/movie/<int:movie_id> return correct content type
        """
        populate_database.populate_with_dummy_data()
        tester = app.test_client()
        response = tester.get('/api/movie/1', follow_redirects=True)
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    def test_get_movie_data(self):
        """
        Test for correct content in response
        """
        # test for response if no entry in DB
        tester = app.test_client()
        response = tester.get('/api/movie/0', follow_redirects=True)
        self.assertTrue(b'Movie with this ID does not exist.' in response.data)

        # test for response if entry in DB
        populate_database.populate_with_dummy_data()
        tester = app.test_client()
        response = tester.get('/api/movie/1', follow_redirects=True)
        with app.app_context():
            movie = movie_service.get_movie_by_id(1)
        self.assertTrue(movie.title.encode() in response.data)

    def test_post_add_movie(self):
        """
        Test post method for movies
        """
        # test with correct input
        tester = app.test_client()
        payload = json.dumps({
            'title': 'Test Title',
            'year': 2000,
            'director': 'Test Director',
            'genre': 'Test Genre'
        })
        response = tester.post('/api/movies', data=payload,
                               headers={"Content-Type": "application/json"},
                               follow_redirects=True)
        statuscode = response.status_code
        data = response.data
        self.assertEqual(statuscode, 200)
        self.assertTrue(b'Movie added successfully!' in data)

        # test with wrong input
        tester = app.test_client()
        payload = json.dumps({
            'title': '',
            'year': 2000,
            'director': '',
            'genre': 'Test Genre'
        })
        response = tester.post('/api/movies', data=payload,
                               headers={"Content-Type": "application/json"},
                               follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    def test_delete_movie(self):
        """
        Test delete method for movie
        """
        tester = app.test_client()
        response = tester.delete('/api/movie/0', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)
        populate_database.populate_with_dummy_data()
        response = tester.delete('/api/movie/1', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
