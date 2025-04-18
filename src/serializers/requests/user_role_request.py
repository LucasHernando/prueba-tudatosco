from marshmallow import Schema, fields, validate

class UserRoleSchema(Schema):
    role_id = fields.Int(required=True)
    user_ids = fields.List(fields.Int(), required=True, validate=validate.Length(min=1))
