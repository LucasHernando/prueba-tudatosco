from querys.session_query import SessionQuerys
from querys.event_query import EventQuerys
from serializers.requests.session_request import SessionSchema
from utils.objects_model import DataResponse, MessagesSessionServices, Attributes, MessagesEventsServices
from http import HTTPStatus


class SessionServices():
    
    session_schema = SessionSchema()
    sessions_schema = SessionSchema(many=True)
    session_querys = SessionQuerys()
    messages = MessagesSessionServices()
    
    
    def service_get_sessions(self, session_id=None, search_event=None, event_id=None):
        
        data_response = DataResponse()
        
        try:
            if session_id:
                session = self.session_querys.get_session_by_id(session_id)
                if not session:
                    
                    data_response.status = HTTPStatus.BAD_REQUEST
                    data_response.message = self.messages.NOT_SEARCH_DATA_SESSION
                 
                    return data_response
                
                
                data_response.data = dict(self.session_schema.dump(session))
                data_response.status = HTTPStatus.OK
                data_response.message = self.messages.RETURN_DATA_LIST_SESSION
                return data_response
            else:
                
                if search_event:
                    sessions = self.session_querys.get_search_event(event_search=search_event)
                else:
                    if event_id:
                        sessions = self.session_querys.get_all_by_event(event_id=event_id)
                    else:
                        sessions = self.session_querys.get_all_sessions()
                                
                data_response.data = self.sessions_schema.dump(sessions)
                data_response.status = HTTPStatus.OK
                data_response.message = self.messages.RETURN_DATA_LIST_SESSION
                
                return data_response
        except Exception as ex:
            data_response.data = []
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_DATA_LIST_SESSION
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
            return data_response
            

    
    def service_create_session(self, data:dict):
        data_response = DataResponse()
        
        try:
            errors = self.session_schema.validate(data)
            
            if errors:
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.message = self.messages.ERROR_CREATE_VALIDATE
                data_response.errors = [{Attributes.ERROR_ATTRIBUTE:errors}]
                
                return data_response
            
            #validate_capacity_schedules_sessions
            self.__validate_capacity_schedules_sessions(data=data)
                
            session = self.session_querys.create_session(data=data)
            
            data_response.data = [{Attributes.ID_ATTRIBUTE: session.id}]
            data_response.status = HTTPStatus.CREATED
            data_response.message = self.messages.CREATION_SESSION
            
            return data_response
        except Exception as ex:
            data_response.data = []
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_CREATION_SESSION
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
            return data_response

    
    def service_update_session(self, session_id:int, data:dict):
        
        data_response = DataResponse()
        
        try:
            role = self.session_querys.get_session_by_id(session_id)
            
            if not role:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_SEARCH_DATA_SESSION
                
                return data_response
            
            errors = self.session_schema.validate(data)
            
            print("errors_session_update**", errors)
            if errors:
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.message = self.messages.ERROR_UPDATE_VALIDATE
                data_response.errors = [{Attributes.ERROR_ATTRIBUTE:errors}]
                
                return data_response
            
            #validate_capacity_schedules_sessions
            self.__validate_capacity_schedules_sessions(data=data)     
            updated = self.session_querys.update_session(session_id=session_id,data=data)
            
            data_response.data = [self.session_schema.dump(updated)]
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.UPDATED_SESSION
        
            return data_response
        except Exception as ex:
            data_response.data = []
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_UPDATE_SESSION
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
            return data_response

    
    def service_delete_session(self, session_id:int):
        
        data_response = DataResponse()
        try:        
            session = self.session_querys.get_session_by_id(session_id)
            if not session:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_SEARCH_DATA_SESSION
                return data_response
                    
            self.session_querys.delete_session(session)
            
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.RETURN_DELETE_SESSION
        
        except Exception as ex:
            data_response.data = []
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_DELETE_SESSION
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
        return data_response
    
    
    def __validate_capacity_schedules_sessions(self, data:dict):
        data_response = DataResponse()
        event_querys = EventQuerys()
        
        event_id = data["event_id"]
        requested_capacity = data["capacity"]
        start_time = data["start_time"]
        end_time = data["end_time"]
        
        message_event = MessagesEventsServices()
        
        if event_id:
            event = event_querys.get_event_by_id(event_id=event_id)
            if not event:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = message_event.NOT_SEARCH_DATA_EVENT
                
                return data_response
        
        if event_id and start_time and end_time:
            conflicting_session = self.session_querys.search_schedules_sessions(data=data)
            if conflicting_session:
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.message = self.messages.CONFLICT_SESSIONS
                
                return data_response
        
        if event and requested_capacity:
            if requested_capacity > event.capacity:
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.message = self.messages.EXCEEDS_CAPACITY_SESSION
            
            return data_response