from cinemate_app import db
from ..models import Review


def get_all_reviews():
    return Review.query.all()


def get_review_by_id(review_id):
    return Review.query.get(review_id)


def delete_review(review):
    db.session.delete(review)
    db.session.commit()


def add_review(movie, nickname, score, comment):
    new_review = Review(nickname=nickname, score=score, comment=comment, movie=movie)
    db.session.add(new_review)
    db.session.commit()


def update_review(current_review, nickname, score, comment):
    current_review.nickname = nickname
    current_review.score = score
    current_review.comment = comment
    db.session.commit()
