from cinemate_app import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(150), nullable=False)
    reviews = db.relationship('Review', cascade="all,delete", backref='movie', lazy=True)

    def calculate_score(self):
        if not self.reviews:
            return "-"
        return round(sum(review.score for review in self.reviews) / len(self.reviews), 1)

    def __repr__(self):
        return f"Movie {self.id} - {self.title}"

    def __init__(self, title, year, director, genre, reviews=None):
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre
        if reviews is None:
            reviews = []
        self.reviews = reviews
