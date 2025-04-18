from marshmallow import Schema, fields, validate

class RoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2))