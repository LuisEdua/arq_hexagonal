from datetime import datetime
from Database.SQL import SessionLocal
from typing import Any
from UserManagement.Domain.Port.UserPort import UserPort
from UserManagement.Domain.Entity.User import User


class UserMySQLRepository(UserPort):
    def __init__(self):
        self.db = SessionLocal()

    def update_verified_at(self, user: User) -> Any:
        user.verified_at = datetime.now()

    def register(self, name: str, lastname: str, cellphone: str, email: str, password: str) -> Any:
        user = User(name, lastname, cellphone, email, password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def search_user_by_token(self, token: str) -> Any:
        return self.db.query(User).filter(User.activation_token == token).first()
