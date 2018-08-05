from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property

from .. import db
from . import BaseModel


class User(BaseModel):
    """User table"""

    def __repr__(self):
        return f"<User: {self.email}>"

    # Attributes
    email = db.Column(db.String(255), index=True, unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    middle_name = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    # Relationships
    ratings = db.relationship("Rating", back_populates="user")
    tasks = db.relationship("Task", back_populates="user")

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    @hybrid_property
    def email_username(self):
        return self.email.split("@")[0]

    @hybrid_property
    def email_domain(self):
        return self.email.split("@")[1]
