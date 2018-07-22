from .. import db
from . import BaseModel


class Movie(BaseModel):
    """
    Movies Details Table
    """

    def __repr__(self):
        return f"<Movie: {self.title}>"

    # Attributes
    description = db.Column(db.Text())
    title = db.Column(db.String(255))
    release_year = db.Column(db.Integer())

    # Relationships
    ratings = db.relationship("Rating", back_populates="movie")
