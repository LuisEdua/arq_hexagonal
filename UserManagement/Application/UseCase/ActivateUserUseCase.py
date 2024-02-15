from typing import Union
from UserManagement.Infrestructure.Repository.Models.UserMySQLModel import User
from UserManagement.Domain.Port.UserPort import UserPort
from typing import Union

class ActivateUserUseCase:
    def __init__(self, repository: UserPort):
        self.repository = repository

    def run(self, token: str) -> Union[User, None]:
        try:
            user = self.repository.search_user_by_token(token)
            new = self.repository.update_verified_at(user.uuid)
            return new
        except Exception as e:
            return None
