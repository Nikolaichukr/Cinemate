from cinemate_app import db
from ..models import Review


def get_all_reviews():
    reviews = Review.query.all()
    return reviews


def get_review_by_id(review_id):
    review = Review.query.get(review_id)
    return review
