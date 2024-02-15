from datetime import datetime
from UserManagement.Domain.Entity.User import User
from UserManagement.Infrestructure.Repository.Models.UserMongoDBModel import UserMongoModel

class UserMongoRepository:
    def __init__(self):
        self.user_model = UserMongoModel()

    def update_verified_at(self, user_id: str) -> Any:
        user_model = self.user_model.find_user({"uuid": user_id})
        if user_model:
            user_model['verified_at'] = datetime.now()
            self.user_model.update_user({"uuid": user_id}, {"$set": user_model})
        return user_model

    def register(self, name: str, lastname: str, cellphone: str, email: str, password: str) -> Any:
        user = User(name, lastname, cellphone, email, password)
        user_model = {
            "uuid": str(user.uuid), 
            "name": user.name, 
            "last_name": user.last_name, 
            "cellphone": user.cellphone,
            "email": user.email, 
            "password": user.password, 
            "activation_token": user.activation_token,
            "verified_at": user.activated_at
        }
        self.user_model.insert_user(user_model)
        return user

    def search_user_by_token(self, token: str) -> Any:
        return self.user_model.find_user({"activation_token": token})