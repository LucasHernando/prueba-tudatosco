from querys.event_query import EventQuerys
from serializers.requests.event_request import EventSchema, EventUpdateSchema
from utils.objects_model import DataResponse, MessagesEventsServices, Attributes, ValidateDataAttributes, EventAttributes, EventStates
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime


class EventServices:
    
    event_schema = EventSchema()
    events_schema = EventSchema(many=True)
    event_querys = EventQuerys()
    messages = MessagesEventsServices()


    def service_create_event(self, data:dict):
        """Crear un nuevo evento"""
        #data = request.get_json()
        
        data_response = DataResponse()

        try:
            # Validaciones básicas
            errors = self.event_schema.validate(data)
            
            if errors:
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.message = self.messages.FIELDS_REQUIRED_EVENT
                data_response.errors = [{Attributes.ERROR_ATTRIBUTE:errors}]
                
                return data_response
        
        
            current_user_id = get_jwt_identity()
            
            event_data = {
                EventAttributes.TITLE:data[EventAttributes.TITLE],
                EventAttributes.DESCRIPTION:data[EventAttributes.DESCRIPTION],
                EventAttributes.CAPACITY:data[EventAttributes.CAPACITY],
                EventAttributes.STATUS:EventStates.PROGRAMMED,
                EventAttributes.START_DATE:datetime.fromisoformat(str(data[EventAttributes.START_DATE])),
                EventAttributes.END_DATE:datetime.fromisoformat(str(data[EventAttributes.END_DATE])),
                EventAttributes.CREATED_BY:current_user_id
            }
            
            
            event = self.event_querys.create_event(data=event_data)
            
            
            data_response.data = [{Attributes.EVENT_ID_ATTRIBUTE: event.id}]
            data_response.status = HTTPStatus.CREATED
            data_response.message = self.messages.CREATION_EVENT
            
            return data_response

            """event = Event(
                title=data["title"],
                description=data["description"],
                status="programado",
                capacity=data["capacity"],
                start_date=datetime.fromisoformat(data["start_date"]),
                end_date=datetime.fromisoformat(data["end_date"]),
                created_by=current_user_id
            )
            db.session.add(event)
            db.session.commit()"""
            
            

            #return jsonify({"msg": "Evento creado exitosamente", "event_id": event.id}), 201
        except Exception as ex:
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_DATA_LIST_EVENT
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
            return data_response

    def service_get_events(self, event_id=None, search_title=None, page=None, per_page=None):
        """Obtener eventos (todos o uno por ID)"""
        
        data_response = DataResponse()
        
        if event_id:
            event = self.event_querys.get_event_by_id(event_id=event_id)
            if not event:
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.message = self.messages.NOT_SEARCH_DATA_EVENT
                 
                return data_response
            
            data_response.data = dict(self.event_schema.dump(event))
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.RETURN_DATA_LIST_EVENT
            return data_response
        else:
            if search_title:
                events = self.event_querys.get_search_title_like(title_search=search_title)
            else:
                #if page:
                events = self.event_querys.get_all_paginate_events(page=None, per_page=None)
                pagination = {
                    "page": events.page,
                    "per_page": events.per_page,
                    "total_pages": events.pages,
                    "total_items": events.total,
                    "has_next": events.has_next,
                    "has_prev": events.has_prev,
                }
                #else:
                #    events = self.event_querys.get_all_events()
                #    pagination
                
            data_response.data = {"data":self.events_schema.dump(events),"pagination": pagination} 
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.RETURN_DATA_LIST_EVENT
            
            return data_response

    def service_update_event(self, event_id:int, data:dict):
        
        data_response = DataResponse()
        event_update_schema = EventUpdateSchema()
        
        try:
            event = self.event_querys.get_event_by_id(event_id=event_id)
            
            if not event:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_SEARCH_DATA_EVENT
                
                return data_response
            
            #data = request.get_json()
            errors = event_update_schema.validate(data)
            if errors:
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.message = self.messages.ERROR_UPDATE_VALIDATE
                data_response.errors = [{Attributes.ERROR_ATTRIBUTE:errors}]
                
                return data_response
                
            updated = self.event_querys.update_event(event_id=event_id, data=data)
            
            data_response.data = [self.event_schema.dump(updated)]
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.CREATION_EVENT
        
            return data_response
        except Exception as ex:
            data_response.data = []
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_DATA_LIST_EVENT
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
            return data_response
    

    def service_delete_event(self, event_id:int):
        
        data_response = DataResponse()
        try:        
            event = self.event_querys.get_event_by_id(event_id=event_id)
            if not event:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_SEARCH_DATA_EVENT
                return data_response
            
            current_user_id = get_jwt_identity()
            print("event.created_by-", event.created_by)
            print("current_user_id", current_user_id)
            
            if int(event.created_by) != int(current_user_id):
                data_response.status = HTTPStatus.FORBIDDEN
                data_response.message = self.messages.ACCESS_DENIED
                return data_response
                
                    
            self.event_querys.delete_event(event=event)
            
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.RETURN_DELETE_EVENT
        
        except Exception as ex:
            data_response.data = []
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_DATA_LIST_EVENT
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
        return data_response