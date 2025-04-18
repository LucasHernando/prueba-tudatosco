from database.db_sqlalchemy import db
from datetime import datetime

class Session(db.Model):
    __tablename__ = 'sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    room = db.Column(db.String(50), nullable=True)
    
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)
    speaker_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    attendances = db.relationship("Attendance", backref="session", lazy=True)

