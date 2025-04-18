from database.db_sqlalchemy import db

class RolePermission(db.Model):
    __tablename__ = 'role_permissions'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id", ondelete="CASCADE"))
    permission_id = db.Column(db.Integer, db.ForeignKey("permissions.id", ondelete="CASCADE"))
    
    
    role = db.relationship("Role", backref=db.backref("role_permissions", cascade="all, delete-orphan"))
    permission = db.relationship("Permission", backref=db.backref("role_permissions", cascade="all, delete-orphan", viewonly=True))