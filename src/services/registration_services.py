from querys.session_query import SessionQuerys
from querys.event_query import EventQuerys
from querys.registration_query import RegistrationQuerys
from serializers.requests.registration_request import RegistrationSchema
from utils.objects_model import DataResponse, MessagesRegistrationServices, Attributes, MessagesEventsServices
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import get_jwt_identity

class RegistrationServices:
    
    registration_schema = RegistrationSchema()
    registrations_schema = RegistrationSchema(many=True)
    registration_querys = RegistrationQuerys()
    messages = MessagesRegistrationServices()
    
    
    def service_register_user_to_event(self, data:dict):
        
        data_response = DataResponse()
        
        user_id = get_jwt_identity()
        data["user_id"] = user_id
        
        errors = self.registration_schema.validate(data)
        
        
        event_id = data["event_id"]
        
            
        if errors:
            data_response.status = HTTPStatus.BAD_REQUEST
            data_response.message = self.messages.ERROR_CREATE_VALIDATE
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE:errors}]
            
            return data_response
    
        event_querys = EventQuerys()
        event = event_querys.get_event_by_id(event_id)
        if not event:
            #return {"msg": "Evento no encontrado"}, 404
            data_response.status = HTTPStatus.NOT_FOUND
            data_response.message = self.messages.EVENT_NOT_FOUND
            return data_response

        #current_registrations = Registration.query.filter_by(event_id=event_id).count()
        current_registrations = self.registration_querys.get_event_current_registrations(event_id=event_id)
        if current_registrations >= event.capacity:
            #return {"msg": "Capacidad del evento alcanzada"}, 400
            data_response.status = HTTPStatus.BAD_REQUEST
            data_response.message = self.messages.OVERLOAD_EVENT
            return data_response
        

        #already_registered = Registration.query.filter_by(user_id=user_id, event_id=event_id).first()
        already_registered = self.registration_querys.get_events_already_registered(user_id=user_id, event_id=event_id)
        if already_registered:
            #return {"msg": "Ya estás registrado en este evento"}, 400
            data_response.status = HTTPStatus.BAD_REQUEST
            data_response.message = self.messages.EXIST_REGISTRED_EVENT
            return data_response

        #registration = Registration(user_id=user_id, event_id=event_id)
        #db.session.add(registration)
        

        try:
            #db.session.commit()
            registration = self.registration_querys.create_registration(data=data)
            #return {"msg": "Registro exitoso"}, 201
            
            data_response.data = [{Attributes.ID_ATTRIBUTE: registration.id}]
            data_response.status = HTTPStatus.CREATED
            data_response.message = self.messages.CREATION_REGISTRED_EVENT
        except IntegrityError as ex:
            self.registration_querys.execute_rollback()
            #return {"msg": "Error al registrar"}, 500
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_CREATE_VALIDATE
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
        return data_response


    def service_get_registered_events_by_user(self, user_id:int):
        #registrations = Registration.query.filter_by(user_id=user_id).all()
        data_response = DataResponse()
        
        if not user_id:
            user_id = get_jwt_identity()
        
         
        try:
            registrations = self.registration_querys.get_registered_events_by_user(user_id=user_id)
            data = [{
                "event_id": r.event_id,
                "registered_at": r.registered_at.isoformat()
            } for r in registrations]
            
            data_response.data = data
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.RECOREDED_EVENTS
        except Exception as ex:
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_DATA_LIST_EVENTS
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
        return data_response
        
        
