from flask.views import MethodView
from flask_jwt_extended import jwt_required
from services.session_services import SessionServices
from utils.http_response import http_response
from flask import request
from flasgger import swag_from
from utils.mockups_enpoints import MackupsSwagger
from utils.objects_model import Permissions
from decorators.permission_required import permission_required

class SessionAPI(MethodView):
    
    
    services = SessionServices()

    
    def post(self):
        data = request.get_json()
        service = self.services.service_create_session(data=data)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)

        
    @jwt_required()
    @swag_from(MackupsSwagger.GET_SESSION)
    @permission_required(Permissions.GET_SESSION)
    def get(self, session_id=None):
        search = request.args.get("event")
        event_id = request.args.get('event_id', default=0, type=int)
        service = self.services.service_get_sessions(session_id=session_id,search_event=search, event_id=event_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
        

    @jwt_required()
    @swag_from(MackupsSwagger.UPDATE_SESSION)
    @permission_required(Permissions.PUT_SESSION_UPDATE)
    def put(self, session_id):
        data = request.get_json()
        service = self.services.service_update_session(data=data, session_id=session_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
        

    @jwt_required()
    @swag_from(MackupsSwagger.DELETE_SESSION)
    @permission_required(Permissions.DEL_SESSION_DELETE)
    def delete(self, session_id):
        service = self.services.service_delete_session(session_id=session_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)