from serializers.requests.user_requests import UserSchema
from models.user_model import User
from database.db_sqlalchemy import db
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta
from utils.objects_model import DataResponse, Attributes, MessagesUsersServices
from querys.user_query import UserQuerys
from http import HTTPStatus
from utils.jwt_custom_claims import build_jwt_data
from serializers.responses.detail_user_response import user_detail_schema
from flask_jwt_extended import get_jwt_identity

class AuthServices:
    
    schema = UserSchema()
    messages = MessagesUsersServices()
    user_querys = UserQuerys()
    
    def service_user_create(self, data:dict):
        
        data_response = DataResponse()

        # Validate data
        try:
            
            data[Attributes.PASSWORD_ATTRIBUTE] = generate_password_hash(data[Attributes.PASSWORD_ATTRIBUTE])
            validated_data = self.schema.load(data)
        except ValidationError as err:
            
            data_response.status = HTTPStatus.BAD_REQUEST
            data_response.message = self.messages.ERROR_VALIDATE_CREATE_USER
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE:  err.messages}]
            
            return data_response
        

        # Create user
        #new_user = User(**validated_data)

        try:
            
            user = self.user_querys.create_user(validated_data)
            
            data_response.data = [{Attributes.ID_ATTRIBUTE: user.email}]
            data_response.status = HTTPStatus.CREATED
            data_response.message = self.messages.CREATION_USER
            
            return data_response
        except Exception as ex:
            db.session.rollback()
            
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_CREATE_USER
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
            return data_response
            
            
            #return {'error': 'Error al crear el usuario', 'details': str(e)}, 500
        
        
    def validate_login(self, data:dict):
        
        data_response = DataResponse()
        
        
        try:
            email = data[Attributes.EMAIL_ATTRIBUTE]
            password = data[Attributes.PASSWORD_ATTRIBUTE]
            
            #user = User.query.filter_by(email=email).first()
            user = self.user_querys.get_user_by_email(email=email)
            if user and check_password_hash(user.password, password):
                # Genera token con duración de 1 hora
                
                access_token = create_access_token(
                identity=str(user.id),
                expires_delta=timedelta(hours=1),
                additional_claims=build_jwt_data(user)  
                )

                data_response.message = MessagesUsersServices.CORRECT_LOGIN
                data_response.status = HTTPStatus.OK
                data_response.data = {"access_token": access_token, "email":user.email}
                
                return data_response
            else:
                
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.CREDENTIALS_INVALID
                return data_response
        except Exception as ex:
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_LOGIN
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
            return data_response
        

    def serivce_detail_user_events(self):
        
        data_response = DataResponse()
        user = user = self.user_querys.get_user_by_id(get_jwt_identity())

        try:
            if not user:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.ERROR_VALIDATE_CREATE_USER
                data_response.errors = [{Attributes.USER_ATTRIBUTE:  self.messages.USER_DETAIL_NOT_FOUND}]
                
                return data_response

            # Obtener roles y eventos registrados
            user_data = {
                "email": user.email,
                "active": user.active,
                "roles": user.roles,
                "events": [registration.event for registration in user.registrations]
            }

            
            data_response.data = user_detail_schema.dump(user_data)
            data_response.message = self.messages.CORRECT_RETURN_DATA_USER
            data_response.status = HTTPStatus.OK
            
        except Exception as ex:
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_DETAIL_USER
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
        
        return data_response
