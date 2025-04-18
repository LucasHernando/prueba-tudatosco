from flask.views import MethodView
from flask_jwt_extended import jwt_required
from services.role_services import RoleServices
from utils.http_response import http_response
from flask import request

class RoleAPI(MethodView):
    
    services = RoleServices()

    @jwt_required()
    def get(self, role_id=None):
        service = self.services.service_get_roles(role_id=role_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
        

    @jwt_required()
    def post(self):
        data = request.get_json()
        service = self.services.service_create_role(data=data)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
        

    @jwt_required()
    def put(self, role_id):
        data = request.get_json()
        service = self.services.service_update_role(data=data, role_id=role_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
        

    @jwt_required()
    def delete(self, role_id):
        service = self.services.service_delete_role(role_id=role_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
        
