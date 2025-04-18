from models.user_model import User
from database.db_sqlalchemy import db


class UserQuerys:
    
    def get_user_by_email(self, email:str):
        return User.query.filter_by(email=email).first()
    
    def get_user_by_id(self, user_id:int):
        return User.query.get(user_id)

    def create_user(self, data):
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user
    
    def get_all_list_users(self, user_ids:list):
        return User.query.filter(User.id.in_(user_ids)).all()