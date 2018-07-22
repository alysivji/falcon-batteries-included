from marshmallow import fields, Schema, ValidationError


class PaginationSchema(Schema):
    # Fields
    page = fields.Int()
    per_page = fields.Int()

    # Validators
    def validate_page(self, data):
        if data < 1:
            raise ValidationError("Page needs to be greater than 0")
