"""
This module contains classes to work with reviews via RESTful API.
"""
from flask_restful import Resource
from cinemate_app.service import review_service
from .utils import INVALID_REVIEW_MESSAGE, NO_REVIEW, review_parser, review_validator


class ReviewList(Resource):
    """
    This class contains methods for /api/reviews route.
    It allows to fetch all the reviews from DB.
    """

    @staticmethod
    def get():
        """
        This method is called when GET requests is received.
        It enables user to fetch all the reviews.

        :return: list of the reviews in JSON format or error message.
        """
        reviews = review_service.get_all_reviews()
        if reviews:
            return [review.as_dict() for review in reviews]
        return {'message': 'There are no reviews in DB right now.'}


class Review(Resource):
    """
    This class contains methods for /api/review/<int:review_id> route.
    It allows to perform fetch, update and delete reviews by id.
    """

    @staticmethod
    def get(review_id):
        """
        This method is called when GET request is received.
        It enables user to fetch review by id.

        :param review_id: id of the review.
        :return: review as JSON or error message.
        """
        review = review_service.get_review_by_id(review_id)
        if review is None:
            return {'message': NO_REVIEW}, 404
        return review.as_dict()

    @staticmethod
    def put(review_id):
        """
        This method is called when PUT request is received.
        It enables user to update existing reviews via API.

        :param review_id: id of the review.
        :return: info message (error / success).
        """
        review = review_service.get_review_by_id(review_id)
        if review is None:
            return {'message': NO_REVIEW}, 404
        args = review_parser.parse_args()
        if not review_validator(args):
            return {'message': INVALID_REVIEW_MESSAGE}, 400
        review_service.update_review(current_review=review, nickname=args['nickname'],
                                     score=args['score'], comment=args['comment'])
        return {'message': 'Review was updated successfully!'}

    @staticmethod
    def delete(review_id):
        """
        This method is called when DELETE request is received.
        It enables user to delete review from DB using review_id via API.

        :param review_id: id of the review.
        :return: info message (success or error).
        """
        review = review_service.get_review_by_id(review_id)
        if review is None:
            return {'message': NO_REVIEW}, 404
        review_service.delete_review(review)
        return {'message': 'This review was successfully deleted.'}
