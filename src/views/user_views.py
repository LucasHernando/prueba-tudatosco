from flask import request
from flask.views import MethodView
from services.user_services import AuthServices
from utils.http_response import http_response
from flask_jwt_extended import jwt_required

class UserAPI(MethodView):
    services = AuthServices()
    
    def post(self):
        data = request.get_json()
        service = self.services.service_user_create(data=data)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
    
    @jwt_required()
    def get(self):
        service = self.services.serivce_detail_user_events()
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
    

class LoginAPI(MethodView):
    services = AuthServices()
    
    def post(self):
        data = request.get_json()
        service = self.services.validate_login(data)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)