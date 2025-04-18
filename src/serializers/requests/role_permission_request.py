from marshmallow import Schema, fields, validate

class RolePermissionSchema(Schema):
    role_id = fields.Int(required=True)
    permission_ids = fields.List(fields.Int(), required=True, validate=validate.Length(min=1))