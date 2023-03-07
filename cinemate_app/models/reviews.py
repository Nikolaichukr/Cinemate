from cinemate_app import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(70), nullable=False)
    score = db.Column(db.Integer, nullable=False, default=0)
    comment = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "score": self.score,
            "comment": self.comment,
            "movie_id": self.movie_id
        }

    def __repr__(self):
        return f"Review {self.id} - {self.nickname} ({self.score})"

    def __init__(self, nickname, score, comment, movie):
        self.nickname = nickname
        self.score = score
        self.comment = comment
        self.movie = movie
