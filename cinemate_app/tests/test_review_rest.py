import json
from cinemate_app import app
from cinemate_app.service import populate_database, review_service
from cinemate_app.tests.test_base import Base


class ReviewsAPITest(Base):
    """
    Class for review rest API test cases
    """

    def test_get_reviews(self):
        """
        Test if /api/reviews is working
        """
        tester = app.test_client()
        response = tester.get('/api/reviews', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_reviews_content_type(self):
        """
        Test if /api/reviews return correct content type
        """
        tester = app.test_client()
        response = tester.get('/api/reviews', follow_redirects=True)
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    def test_get_reviews_data(self):
        """
        Test for correct content in response from /api/reviews
        """
        populate_database.populate_with_dummy_data()
        tester = app.test_client()
        response = tester.get('/api/reviews', follow_redirects=True)
        with app.app_context():
            review = review_service.get_review_by_id(1)
        self.assertTrue(review.comment.encode() in response.data)

    def test_get_review(self):
        """
        Test if /api/review/<int:review_id> is working
        """
        populate_database.populate_with_dummy_data()
        tester = app.test_client()
        response = tester.get('/api/review/1', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_review_content_type(self):
        """
        Test if /api/review/<int:review_id> return correct content type
        """
        populate_database.populate_with_dummy_data()
        tester = app.test_client()
        response = tester.get('/api/review/1', follow_redirects=True)
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    def test_get_review_data(self):
        """
        Test for correct content in response from /api/review/<int:review_id>
        """
        # test for response if no entry in DB
        tester = app.test_client()
        response = tester.get('/api/review/0', follow_redirects=True)
        self.assertTrue(b'Review with this ID does not exist.' in response.data)

        # test for response if entry in DB
        populate_database.populate_with_dummy_data()
        response = tester.get('/api/review/1', follow_redirects=True)
        with app.app_context():
            review = review_service.get_review_by_id(1)
        self.assertTrue(review.comment.encode() in response.data)

    def test_post_add_review(self):
        """
        Test post method for adding reviews on /api/movie/<int:movie_id>
        """
        # test with correct input
        tester = app.test_client()
        populate_database.populate_with_dummy_data()
        payload = json.dumps({
            'nickname': 'ProfessionalReviewer',
            'score': 10,
            'comment': 'Some test review'
        })
        response = tester.post('/api/movie/1', data=payload,
                               headers={"Content-Type": "application/json"},
                               follow_redirects=True)
        statuscode = response.status_code
        data = response.data
        self.assertEqual(statuscode, 200)
        self.assertTrue(b'was added successfully' in data)

        # test with wrong input
        payload = json.dumps({
            'nickname': '',
            'score': 11,
            'comment': 'Some test review'
        })
        response = tester.post('/api/movie/1', data=payload,
                               headers={"Content-Type": "application/json"},
                               follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

        # test with non-existing movie
        payload = json.dumps({
            'nickname': '',
            'score': 11,
            'comment': 'Some test review'
        })
        response = tester.post('/api/movie/0', data=payload,
                               headers={"Content-Type": "application/json"},
                               follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    def test_put_update_review(self):
        """
        Test put method to update review on /api/review/<int:review_id>
        """
        tester = app.test_client()
        populate_database.populate_with_dummy_data()
        payload = json.dumps({
            'nickname': 'UpdatedReviewer',
            'score': 9,
            'comment': 'Some updated review for test'
        })
        # test for existing review with correct data
        response = tester.put('/api/review/1', data=payload,
                              headers={"Content-Type": "application/json"},
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # test for non-existing review
        response = tester.put('/api/review/0', data=payload,
                              headers={"Content-Type": "application/json"},
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

        # test with incorrect data
        payload = json.dumps({
            'nickname': '',
            'score': 11,
            'comment': '-'
        })
        # test for existing review with correct data
        response = tester.put('/api/review/1', data=payload,
                              headers={"Content-Type": "application/json"},
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    def test_delete_review(self):
        """
        Test delete method for review with /api/review/<int:review_id>
        """
        tester = app.test_client()
        response = tester.delete('/api/review/0', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)
        populate_database.populate_with_dummy_data()
        response = tester.delete('/api/review/1', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
