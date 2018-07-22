from .. import db
from . import BaseModel


class Rating(BaseModel):
    """
    Movie Ratings for user
    """

    # Attributes
    movie_id = db.Column(
        db.Integer(), db.ForeignKey("movie.id", name="fk_rating_movie_id")
    )
    rating = db.Column(db.Integer())
    user_id = db.Column(
        db.Integer(), db.ForeignKey("user.id", name="fk_rating_user_id")
    )

    # Relationships
    movie = db.relationship("Movie", back_populates="ratings")
    user = db.relationship("User", back_populates="ratings")
