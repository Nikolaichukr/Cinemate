from cinemate_app import app
from cinemate_app.service import populate_database
from cinemate_app.tests.test_base import Base


class ReviewsTest(Base):
    """
    Class for review views test cases
    """

    def test_reviews(self):
        """
        Test /reviews views with and without entries in DB
        """
        tester = app.test_client()
        response = tester.get('/reviews/', content_type='html/text')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        populate_database.populate_with_dummy_data()
        tester = app.test_client()
        response = tester.get('/reviews/', content_type='html/text')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_movie(self):
        """
        Test /reviews/review/<int:review_id> views with get method
        """
        # if review doesn't exist
        tester = app.test_client()
        response = tester.get('/reviews/review/0')
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)

        # if review exists
        tester = app.test_client()
        populate_database.populate_with_dummy_data()
        response = tester.get('/reviews/review/1')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_add_review(self):
        """
        Test /reviews/add_review/<int:movie_id> views with get and post methods.
        """
        # test add review view with get method
        tester = app.test_client()
        populate_database.populate_with_dummy_data()
        response = tester.get('/reviews/add_review/1')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # test add review view with post method
        populate_database.populate_with_dummy_data()
        tester = app.test_client()
        response = tester.post('/reviews/add_review/1',
                               data={'nickname': 'TestNickname',
                                     'score': 10,
                                     'comment': 'TestComment'},
                               follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # test add review view with post method for the movie that does not exist
        tester = app.test_client()
        response = tester.post('/reviews/add_review/0',
                               data={'nickname': 'TestNickname',
                                     'score': 10,
                                     'comment': 'TestComment'},
                               follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_update_review(self):
        """
        Test /reviews/update_review/<int:review_id> views with get and post
        methods, providing correct and incorrect information.
        """
        populate_database.populate_with_dummy_data()
        # test update review providing wrong review_id with get method
        tester = app.test_client()
        response = tester.get('reviews/update_review/0',
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # test update review providing correct movie_id with get method
        tester = app.test_client()
        response = tester.get('reviews/update_review/1',
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # test update review providing correct review_id with post method
        tester = app.test_client()
        response = tester.post('reviews/update_review/1',
                               data={'nickname': 'NewNickname',
                                     'score': 9,
                                     'comment': 'NewComment'},
                               follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_delete_review(self):
        """
        Test /reviews/delete_review/<int:review_id> views with get method.
        """
        populate_database.populate_with_dummy_data()
        # test delete review with correct review_id
        tester = app.test_client()
        response = tester.get('/reviews/delete_review/1',
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # test delete review with review_id that does not exist
        tester = app.test_client()
        response = tester.get('/reviews/delete_review/0',
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
