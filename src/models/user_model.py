import datetime
from database.db_sqlalchemy import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at =db.Column(db.DateTime, default=datetime.datetime.now())
    password = db.Column(db.Text, nullable=False)
    # User fields
    active = db.Column(db.Boolean, default=True)
    
    roles = db.relationship('Role', secondary='user_roles', backref='users')