from marshmallow import fields, post_load, Schema, validates, ValidationError

import falcon

from app import db
from app.exceptions import HTTPError
from app.models import User
from app.utilities import generate_password_hash


class UserExistsSchema(Schema):
    # Fields
    email = fields.Email(required=True)

    # Validators
    @validates("email")
    def validate_email(self, data):
        email = db.query(User).filter(User.email == data).first()
        if not email:
            raise HTTPError(falcon.HTTP_NOT_FOUND, errors={"email": "does not exist"})


class UserSchema(Schema):
    # Fields
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    first_name = fields.String(required=True)
    middle_name = fields.String()
    last_name = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

    # Validators
    @validates("email")
    def validate_email(self, data):
        email = db.query(User).filter(User.email == data).first()
        if email:
            raise ValidationError("Account already exists for email")

    # Loaders
    @post_load
    def make_user(self, data, **kwargs):
        if "password" in data:
            data["password_hash"] = generate_password_hash(data.pop("password"))
        return User(**data)


class UserPatchSchema(Schema):
    first_name = fields.String()
    middle_name = fields.String()
    last_name = fields.Str()
    # TODO allow for changing passwords (need to think about auth strategy)


class UserPathSchema(Schema):
    id = fields.Int()


users_exists_schema = UserExistsSchema()
users_item_schema = UserSchema()
users_patch_schema = UserPatchSchema()
users_path_schema = UserPathSchema()
