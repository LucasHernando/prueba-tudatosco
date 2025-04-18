from models.session_model import Session
from database.db_sqlalchemy import db
from sqlalchemy import and_


class SessionQuerys:
    
    def get_all_sessions(self):
        return Session.query.all()
    
    def get_all_by_event(self, event_id):
        return Session.query.filter_by(event_id=event_id)

    def get_session_by_id(self, role_id):
        return Session.query.get(role_id)

    def create_session(self, data:dict):
        session = Session(**data)
        db.session.add(session)
        db.session.commit()
        return session

    def update_session(self, session_id:int, data:dict):
        session = Session.query.filter_by(id=session_id).update(data)
        db.session.commit()
        return session

    def delete_session(self, session: Session):
        db.session.delete(session)
        db.session.commit()
        
    def search_schedules_sessions(self, data:dict):
        return (Session.query.filter(Session.event_id == data["event_id"],
        and_(
            Session.start_time < data["end_time"],
            Session.end_time > data["start_time"]
        )).first())
        
    def get_search_event(self, event_search:int):
        return Session.query.filter(Session.event_id == event_search).all()