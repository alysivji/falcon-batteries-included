from marshmallow import fields, post_load, Schema, validates, ValidationError

from app.constants import CURRENT_YEAR
from app.models import Movie


class MovieSchema(Schema):
    # Fields
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    release_year = fields.Int(required=True)
    description = fields.Str(required=True)

    # Validators
    @validates("release_year")
    def validate_release_year(self, data):
        if data > CURRENT_YEAR:
            raise ValidationError("Cannot insert unreleased movie")

    # Loaders
    @post_load
    def make_user(self, data):
        return Movie(**data)


movies_list_schema = MovieSchema(many=True)
movies_post_schema = MovieSchema()
