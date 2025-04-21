from flask.views import MethodView
from flask_jwt_extended import jwt_required
from services.event_services import EventServices
from utils.http_response import http_response
from flask import request
from flasgger import swag_from
from utils.mockups_enpoints import MackupsSwagger
from utils.objects_model import Permissions
from decorators.permission_required import permission_required

class EventAPI(MethodView):
    
    
    services = EventServices()

    @jwt_required()
    @swag_from(MackupsSwagger.CREATE_EVENT)
    @permission_required(Permissions.POST_EVENT_CREATE)
    def post(self):
        data = request.get_json()
        service = self.services.service_create_event(data=data)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)

        
    @jwt_required()
    @swag_from(MackupsSwagger.LIST_EVENTS)
    @permission_required(Permissions.GET_LIST_EVENTS)
    def get(self, event_id=None):
        search = request.args.get("search")
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)
        service = self.services.service_get_events(event_id=event_id, search_title=search, page=page, per_page=per_page)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
        

    @jwt_required()
    @swag_from(MackupsSwagger.UPDATE_SESSION)
    @permission_required(Permissions.PUT_SESSION_UPDATE)
    def put(self, event_id):
        data = request.get_json()
        service = self.services.service_update_event(data=data, event_id=event_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
        

    @jwt_required()
    @swag_from(MackupsSwagger.DELETE_SESSION)
    @permission_required(Permissions.DEL_SESSION_DELETE)
    def delete(self, event_id):
        service = self.services.service_delete_event(event_id=event_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
        
