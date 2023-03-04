"""
This module contains form classes to work with movies
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class MovieForm(FlaskForm):
    """Form class to add/update movies in the database"""
    title = StringField(label="Title", validators=[DataRequired(), Length(min=1, max=150)])
    year = IntegerField(label="Year", validators=[DataRequired(),
                                                  NumberRange(min=1900, max=2025,
                                                              message="Enter a number from 1900 to 2025")])
    director = StringField(label="Director", validators=[DataRequired(), Length(min=1, max=100)])
    genre = StringField(label="Genre", validators=[DataRequired(), Length(min=1, max=150)])
    submit = SubmitField(label="Save")


class FilterMovieByYearForm(FlaskForm):
    """Form class to filter movies by date"""
    msg = "Enter a number from 1900 to 2025"
    from_year = IntegerField(label="From Year:",
                             validators=[DataRequired(), NumberRange(min=1900, max=2025, message=msg)])
    to_year = IntegerField(label="To Year:", validators=[DataRequired(), NumberRange(min=1900, max=2025, message=msg)])
    submit = SubmitField(label="Search")
