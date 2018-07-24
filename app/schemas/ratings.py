from marshmallow import fields, Schema, validates, ValidationError


class RatingSchema(Schema):
    # Fields
    rating = fields.Int(required=True)

    # Validators
    @validates("rating")
    def validate_rating(self, data):
        if 1 <= data <= 5:
            return
        raise ValidationError("rating must be between 1 and 5")


rating_item_schema = RatingSchema()
