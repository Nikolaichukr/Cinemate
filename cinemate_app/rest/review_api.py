from flask_restful import Resource
from cinemate_app.service import review_service
from .utils import INVALID_REVIEW_MESSAGE, NO_REVIEW, review_parser, review_validator


class ReviewList(Resource):

    @staticmethod
    def get():
        reviews = review_service.get_all_reviews()
        if reviews:
            return [review.as_dict() for review in reviews]
        return {'Message': 'There are no reviews in DB right now.'}


class Review(Resource):

    @staticmethod
    def get(review_id):
        review = review_service.get_review_by_id(review_id)
        if review is None:
            return {'Message': NO_REVIEW}, 404
        return review.as_dict()

    @staticmethod
    def put(review_id):
        review = review_service.get_review_by_id(review_id)
        if review is None:
            return {'Message': NO_REVIEW}, 404
        args = review_parser.parse_args()
        if not review_validator(args):
            return {'Message': INVALID_REVIEW_MESSAGE}, 400
        review_service.update_review(current_review=review, nickname=args['nickname'], score=args['score'],
                                     comment=args['comment'])
        return {'Message': 'Review was updated successfully!'}

    @staticmethod
    def delete(review_id):
        review = review_service.get_review_by_id(review_id)
        if review is None:
            return {'Message': NO_REVIEW}, 404
        review_service.delete_review(review)
        return {'Message': 'This review was successfully deleted.'}
