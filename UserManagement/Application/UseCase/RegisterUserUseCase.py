from UserManagement.Domain.Entity.User import User
from UserManagement.Domain.Port.UserPort import UserPort
from typing import Union

class RegisterUserUseCase:

    def __init__(self, repository: UserPort):
        self.repository = repository

    def run(self, name, lastname, cellphone, email, password) -> Union[User, None]:
        try:
            return self.repository.register(name, lastname, cellphone, email, password)
        except Exception:
            return None
