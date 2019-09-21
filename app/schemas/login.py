from marshmallow import fields, post_load, Schema

import falcon

from app import db
from app.exceptions import HTTPError
from app.models import User
from app.utilities import password_matches


class LoginSchema(Schema):
    # Fields
    email = fields.Email(required=True)
    password = fields.Str(required=True)

    # Loaders
    @post_load
    def make_user(self, data, **kwargs):
        user = db.query(User).filter(User.email == data["email"]).first()
        if not user or not password_matches(data["password"], user.password_hash):
            raise HTTPError(
                falcon.HTTP_UNAUTHORIZED,
                errors={"message": "Invalid username / password"},
            )
        return user


login_schema = LoginSchema()
