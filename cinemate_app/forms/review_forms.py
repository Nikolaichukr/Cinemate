"""
This module contains form classes to work with reviews.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length


class ReviewForm(FlaskForm):
    """Form class to add/update reviews in the database."""

    nickname = StringField(label="Nickname", validators=[DataRequired(), Length(min=1, max=70)])
    score = IntegerField(label="Score",
                         validators=[DataRequired(),
                                     NumberRange(min=1, max=10,
                                                 message="Enter a number from 1 to 10")])
    comment = TextAreaField(label="Comment", validators=[DataRequired(), Length(min=5, max=2048)])
    submit = SubmitField(label="Save")
