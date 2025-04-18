from flask.views import MethodView
from flask_jwt_extended import jwt_required
from services.role_permission_services import RolePermissionServices
from utils.http_response import http_response
from flask import request
from flasgger import swag_from
from utils.mockups_enpoints import MackupsSwagger
from utils.objects_model import Permissions
from decorators.permission_required import permission_required

class RolePermissionAPI(MethodView):
    
    services = RolePermissionServices()
    
    
    @jwt_required()
    @swag_from(MackupsSwagger.CREATE_ROLE_PERMISSIONS)
    @permission_required(Permissions.POST_ROLE_PERMISSIONS_CREATE)
    def post(self):
        data = request.get_json()
        service = self.services.service_create_role_permissions(data=data)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
    
    @jwt_required()
    @swag_from(MackupsSwagger.DELETE_ROLE_PERMISSIONS)
    @permission_required(Permissions.DEL_ROLE_PERMISSIONS_DELETE)
    def delete(self):
        data = request.get_json()
        service = self.services.service_delete_role_permissions(data=data)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)