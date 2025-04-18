from marshmallow import Schema, fields

class UserRoleListSchema(Schema):
    role_id = fields.Int()
    role_name = fields.Str()
    user_id = fields.Int()
    user_email = fields.Email()
