from UserManagement.Domain.Entity.User import User
from abc import ABC, abstractmethod


class EmailPort(ABC):
    @abstractmethod
    def run(self, user: User) -> None: pass
