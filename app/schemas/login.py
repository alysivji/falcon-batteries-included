from marshmallow import fields, post_load, Schema, validates, ValidationError

from app.utilities import generate_password_hash


class LoginSchema(Schema):
    # Fields
    email = fields.Email(required=True)
    password = fields.Str(required=True)

    # Loaders
    @post_load
    def make_user(self, data):
        if "password" in data:
            data["password_hash"] = generate_password_hash(data.pop("password"))
        return data


login_schema = LoginSchema()
