"""
This module defines `Movie` class - a model to work with movies table.
"""
from cinemate_app import db


class Movie(db.Model):
    """
    Model representing Movie.

    :param str title: title of the movie
    :param int year: the year when movie was released
    :param str director: a name of the person who directed the movie
    :param str genre: movie genre(s)
    :param reviews: movie reviews
    :type reviews: list[Review] or None
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(150), nullable=False)
    reviews = db.relationship('Review', cascade="all,delete", backref='movie', lazy=True)

    def calculate_score(self):
        """
        This function calculates movie score based on existing reviews.

        :return: int or single dash '-'
        :rtype: Union[int, str]
        """
        if not self.reviews:
            return "-"
        return round(sum(review.score for review in self.reviews) / len(self.reviews), 1)

    def as_dict(self):
        """
        This function returns movie information as a dictionary.

        :return: dictionary of movie info
        :rtype: dict
        """
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "director": self.director,
            "genre": self.genre,
            "review_ids": [review.id for review in self.reviews]
        }

    def __repr__(self):
        return f"Movie {self.id} - {self.title}"

    # pylint: disable=too-many-arguments
    def __init__(self, title, year, director, genre, reviews=None):
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre
        if reviews is None:
            reviews = []
        self.reviews = reviews
