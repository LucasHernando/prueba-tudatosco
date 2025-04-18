from marshmallow import Schema, fields, post_dump

class RoleSchema(Schema):
    name = fields.Str()

class EventSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    status = fields.Str()
    capacity = fields.Int()
    start_date = fields.DateTime()
    end_date = fields.DateTime()
    created_at = fields.DateTime()

class UserDetailSchema(Schema):
    id = fields.Int()
    email = fields.Email()
    active = fields.Boolean()
    roles = fields.Nested(RoleSchema, many=True)
    events = fields.Nested(EventSchema, many=True)

    @post_dump
    def fill_empty(self, data, **kwargs):
        # Si no hay roles o eventos, se muestran como listas vacías
        data.setdefault('roles', [])
        data.setdefault('events', [])
        return data


user_detail_schema = UserDetailSchema()
