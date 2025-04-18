from models.user_role_model import UserRoles
from models.user_model import User
from models.role_model import Role
from database.db_sqlalchemy import db
from datetime import datetime


class UserRoleQuerys:
    
    def create_user_role(self, data:dict):
        user_role = UserRoles(**data)
        db.session.add(user_role)
        db.session.commit()
        return user_role
    
    def delete_user_role(self, user_role):
        db.session.delete(user_role)
        db.session.commit()
        
        
    def get_first_role_user(self, role_id:int, user_id:int):
        return UserRoles.query.filter_by(role_id=role_id, user_id=user_id).first()
    
    def get_object(self, role_id:int, user_id:int):
        return UserRoles(role_id=role_id, user_id=user_id)
    
    def add_values_session(self, value):
        return db.session.add(value)
    
    def delete_values_session(self, value):
        return db.session.delete(value)
    
    def add_execute_session(self):
        return db.session.commit()
    
    def get_list_roles_users(self):
        return (db.session.query(
            UserRoles.role_id,
            Role.name.label("role_name"),
            User.id.label("user_id"),
            User.email.label("user_email")
        ).join(Role, Role.id == UserRoles.role_id
        ).join(User, User.id == UserRoles.user_id))
        
    def get_list_role_users(self, role_id=None):
        
        if role_id:
            query = self.get_list_roles_users().filter(UserRoles.role_id == role_id).all()
        else:
            query = self.get_list_roles_users().all()
            
        return query