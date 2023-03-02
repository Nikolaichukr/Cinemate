from flask import Blueprint, render_template
from cinemate_app.service import review_service

reviews = Blueprint('reviews', __name__)


@reviews.route('/')
def reviews_page():
    reviews_list = review_service.get_all_reviews()
    return render_template('reviews.html', title="List of Reviews", reviews_list=reviews_list)


@reviews.route('/review/<int:review_id>')
def review(review_id):
    current_review = review_service.get_review_by_id(review_id)
    return render_template('review.html', review=current_review)


@reviews.route('/add_review')
def add_review():
    return render_template('add_review.html', title="Add Review")


@reviews.route('/update_review')
def update_review():
    return render_template('update_review.html', title="Update Review")
