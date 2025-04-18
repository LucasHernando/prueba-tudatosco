from marshmallow import Schema, fields, validates, ValidationError

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(allow_none=True)
    status = fields.String(dump_default="programmed")
    capacity = fields.Integer(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    
class EventUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=False)
    description = fields.String(required=False)
    status = fields.String(required=False)
    capacity = fields.Integer(required=False)
    start_date = fields.DateTime(required=False)
    end_date = fields.DateTime(required=False)