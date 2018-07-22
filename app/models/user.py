from datetime import datetime

from .. import db
from . import BaseModel


class User(BaseModel):
    """
    User table
    """

    # Attributes
    email = db.Column(db.String(255), index=True, unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    middle_name = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    # Relationships
    ratings = db.relationship("Rating", back_populates="user")
