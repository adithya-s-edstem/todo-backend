from marshmallow import Schema, fields, validate

class TodoSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1, error="Title should not be empty"))
    description = fields.String()
