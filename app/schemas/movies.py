from marshmallow import fields, post_load, Schema, validates, ValidationError

from app.constants import CURRENT_YEAR
from app.models import Movie


class MovieSchema(Schema):
    # Fields
    id = fields.Int(dump_only=True)
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


class MoviePatchSchema(Schema):
    title = fields.Str()
    release_year = fields.Int()
    description = fields.Str()


class MoviePathSchema(Schema):
    id = fields.Int()


class MovieQuerySchema(Schema):
    page = fields.Int(missing=1)
    per_page = fields.Int(missing=20)

    class Meta:
        strict = True


movies_item_schema = MovieSchema()
movies_list_schema = MovieSchema(many=True)
movies_patch_schema = MoviePatchSchema()
movies_path_schema = MoviePathSchema()
movies_query_schema = MovieQuerySchema()
