from models.event_model import Event
from database.db_sqlalchemy import db
from datetime import datetime


class EventQuerys:
    
    def get_all_events(self):
        return Event.query.all()
    
    def get_all_paginate_events(self,page=None, per_page=None):
        return Event.query.paginate(page=page, per_page=per_page, error_out=False)

    def get_event_by_id(self, event_id):
        return Event.query.get(event_id)

    def create_event(self, data:dict):
        event = Event(**data)
        db.session.add(event)
        db.session.commit()
        return event

    def update_event(self, event_id:int, data:dict):
        event = Event.query.filter_by(id=event_id).first()

        if not event:
            return None
        
        
        event.title = data.get("title", event.title)
        event.description = data.get("description", event.description)
        event.status = data.get("status", event.status)
        event.capacity = data.get("capacity", event.capacity)
        event.start_date = datetime.fromisoformat(str(data.get("start_date", event.start_date)))
        event.end_date = datetime.fromisoformat(str(data.get("end_date", event.end_date)))
        
        db.session.commit()
        return event

    def delete_event(self, event):
        db.session.delete(event)
        db.session.commit()
        
        
    def get_search_title_like(self, title_search:str):
        return Event.query.filter(Event.title.ilike(f"%{title_search}%")).all()