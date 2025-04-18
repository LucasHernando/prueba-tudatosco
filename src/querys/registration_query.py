from models.registration_model import Registration
from database.db_sqlalchemy import db


class RegistrationQuerys:
    
    
    def get_event_current_registrations(self, event_id:int):
        return Registration.query.filter_by(event_id=event_id).count()
    
    def get_events_already_registered(self, user_id:int, event_id:int):
        return Registration.query.filter_by(user_id=user_id, event_id=event_id).first()
    

    def create_registration(self, data:dict):
        registration = Registration(**data)
        db.session.add(registration)
        db.session.commit()
        return registration
    

    def get_registered_events_by_user(self, user_id):
        return Registration.query.filter_by(user_id=user_id).all()
    
    def execute_rollback(self):
        return db.session.rollback()
    
