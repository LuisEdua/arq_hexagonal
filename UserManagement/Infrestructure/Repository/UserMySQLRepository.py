from datetime import datetime
from Database.MySQL import SessionLocal
from typing import Any
from UserManagement.Domain.Port.UserPort import UserPort
from UserManagement.Domain.Entity.User import User
from UserManagement.Infrestructure.Repository.Models.UserMySQLModel import User as UserModel

class UserMySQLRepository(UserPort):
    def __init__(self):
        self.db = SessionLocal()

    def update_verified_at(self, user_id: str) -> Any:
        user_model = self.db.query(UserModel).filter(UserModel.uuid == user_id).first()
        user_model.verified_at = datetime.now()
        response = {"uuid": str(user_model.uuid),
            "name": user_model.name,
            "last_name": user_model.last_name,
            "email": user_model.email,
            "cellphone": user_model.cellphone,
            "activated_at": str(user_model.verified_at)
            }
        self.db.commit()
        return response

    def register(self, name: str, lastname: str, cellphone: str, email: str, password: str) -> Any:
        user = User(name, lastname, cellphone, email, password)
        user_model = UserModel(uuid=str(user.uuid), name=user.name, last_name=user.last_name, cellphone=user.cellphone,
                            email=user.email, password=user.password, activation_token=user.activation_token,
                            verified_at=user.activated_at)
        self.db.add(user_model)
        self.db.commit()
        return user

    def search_user_by_token(self, token: str) -> Any:
        return self.db.query(UserModel).filter(UserModel.activation_token == token).first()
