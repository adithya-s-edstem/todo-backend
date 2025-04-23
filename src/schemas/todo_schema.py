from marshmallow import Schema, fields

class TodoSchema(Schema):
    title = fields.String(required=True)
    description = fields.String()
