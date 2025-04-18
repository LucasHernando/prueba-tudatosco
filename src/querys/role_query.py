from models.role_model import Role
from database.db_sqlalchemy import db


class RoleQuerys:
    
    def get_all_roles(self):
        return Role.query.all()

    def get_role_by_id(self, role_id):
        return Role.query.get(role_id)

    def create_role(self, name):
        role = Role(name=name)
        db.session.add(role)
        db.session.commit()
        return role

    def update_role(self, role, new_name):
        role.name = new_name
        db.session.commit()
        return role

    def delete_role(self, role):
        db.session.delete(role)
        db.session.commit()