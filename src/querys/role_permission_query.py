from models.role_permission_model import RolePermission
from database.db_sqlalchemy import db


class RolePermissionQuerys:
    
    def create_role_permission(self, data:dict):
        role_permission = RolePermission(**data)
        db.session.add(role_permission)
        db.session.commit()
        return role_permission
    
    def delete_role_permission(self, role_permission):
        db.session.delete(role_permission)
        db.session.commit()
        
    def get_all_role_permissions(self, role_id):
        return RolePermission.query.filter_by(role_id = role_id).all()
    
    def get_first_role_permission(self, role_id:int, permission_id:int):
        return RolePermission.query.filter_by(role_id=role_id, permission_id=permission_id).first()
    
    def get_object(self, role_id:int, permission_id:int):
        return RolePermission(role_id=role_id, permission_id=permission_id)
    
    def add_values_session(self, value):
        return db.session.add(value)
    
    def delete_values_session(self, value):
        return db.session.delete(value)
    
    def add_execute_session(self):
        return db.session.commit()