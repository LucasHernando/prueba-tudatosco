from models.permission_model import Permission 
from database.db_sqlalchemy import db


class PermissionQuerys:
    
    def get_all_permissions(self):
        return Permission.query.all()
    
    def get_all_list_permissions(self, permission_ids:list):
        return Permission.query.filter(Permission.id.in_(permission_ids)).all()

    def get_permission_by_id(self, role_id):
        return Permission.query.get(role_id)

    def create_permission(self, data:dict):
        permission = Permission(**data)
        db.session.add(permission)
        db.session.commit()
        return permission

    def update_permission(self, permission_id:int, data:dict):
        session = Permission.query.filter_by(id=permission_id).update(data)
        db.session.commit()
        return session

    def delete_permission(self, permission: Permission):
        db.session.delete(permission)
        db.session.commit()