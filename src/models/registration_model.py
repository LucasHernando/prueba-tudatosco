from database.db_sqlalchemy import db
from datetime import datetime

class Registration(db.Model):
    __tablename__ = 'registrations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref="registrations")
