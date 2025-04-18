from marshmallow import Schema, fields, validates_schema, ValidationError
from datetime import datetime

class SessionSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)
    capacity = fields.Int(required=True)
    event_id = fields.Int(required=True)
    speaker_id = fields.Int(required=True)

    @validates_schema
    def validate_times(self, data, **kwargs):
        if data['end_time'] <= data['start_time']:
            raise ValidationError("End time must be after start time.")
        
        
class SessionSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=False)
    description = fields.Str()
    start_time = fields.DateTime(required=False)
    end_time = fields.DateTime(required=False)
    capacity = fields.Int(required=False)
    event_id = fields.Int(required=False)
    speaker_id = fields.Int(required=False)

    @validates_schema
    def validate_times(self, data, **kwargs):
        if data['end_time'] <= data['start_time']:
            raise ValidationError("End time must be after start time.")
