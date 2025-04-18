from marshmallow import Schema, fields, validates, ValidationError

class UserSchema(Schema):
    password = fields.Str(required=True)
    email = fields.Email(required=True)

    @validates('password')
    def validate_username(self, value):
        if len(value) < 10:
            raise ValidationError('El nombre de usuario debe tener al menos 10 caracteres.')
