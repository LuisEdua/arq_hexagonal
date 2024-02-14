from UserManagement.Domain.Entity.User import User
from UserManagement.Domain.Port.UserPort import UserPort
from typing import Union, Any

class RegisterUserUseCase:

    def __init__(self, repository: UserPort):
        self.repository = repository

    async def run(self, name, lastname, cellphone, email, password) -> Union[User, Any]:
        try:
            return await self.repository.register(name, lastname, cellphone, email, password)
        except Exception:
            pass
