from marshmallow import Schema, fields
from datetime import datetime

class RegistrationSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    event_id = fields.Int(required=True)
    registered_at = fields.DateTime(dump_only=True, default=datetime.utcnow)