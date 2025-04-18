from database.db_sqlalchemy import db

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    
    permissions = db.relationship('Permission', secondary='role_permissions', backref='roles', viewonly=True)