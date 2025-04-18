from flask.views import MethodView
from flask_jwt_extended import jwt_required
from services.registration_services import RegistrationServices
from utils.http_response import http_response
from flask import request
from flasgger import swag_from
from utils.mockups_enpoints import MackupsSwagger
from utils.objects_model import Permissions
from decorators.permission_required import permission_required

class RegisterAPI(MethodView):
    
    services = RegistrationServices()
    
    @jwt_required()
    @swag_from(MackupsSwagger.CREATE_REGISTERS)
    @permission_required(Permissions.POST_REGISTRATION_CREATE)
    def post(self):
        data = request.get_json()
        service = self.services.service_register_user_to_event(data=data)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
    
    


    @jwt_required()
    @swag_from(MackupsSwagger.LIST_REGISTERS)
    @permission_required(Permissions.GET_LIST_REGISTRATIONS)
    def get(self, user_id=None):
        service = self.services.service_get_registered_events_by_user(user_id=user_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)