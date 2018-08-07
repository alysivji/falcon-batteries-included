from .. import db
from . import BaseModel, SearchableMixin


class Movie(SearchableMixin, BaseModel):
    """Movies Details Table"""

    __searchable__ = ["description"]

    def __repr__(self):
        return f"<Movie: {self.title}>"

    # Attributes
    description = db.Column(db.Text())
    title = db.Column(db.String(255))
    release_year = db.Column(db.Integer())

    # Relationships
    ratings = db.relationship("Rating", back_populates="movie")
