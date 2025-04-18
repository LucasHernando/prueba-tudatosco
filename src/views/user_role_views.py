from flask.views import MethodView
from flask_jwt_extended import jwt_required
from services.user_role_services import UserRoleServices
from utils.http_response import http_response
from flask import request


class UserRoleAPI(MethodView):
    
    services = UserRoleServices()
    
    @jwt_required()
    def get(self, role_id=None):
        role_id = request.args.get("role_id", type=int)
        #role_id = role_id if role_id else None
        service = self.services.service_get_list_roles_users(role_id=role_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
    
    @jwt_required()
    def post(self):
        data = request.get_json()
        service = self.services.service_create_role_users(data=data)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
    
    @jwt_required()
    def delete(self):
        data = request.get_json()
        service = self.services.service_delete_role_users(data=data)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)