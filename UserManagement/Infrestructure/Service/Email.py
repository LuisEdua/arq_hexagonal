from UserManagement.Domain.Entity.User import User
from UserManagement.Infrestructure.Service.EmailPort import EmailPort

class Email(EmailPort):

    def run(self, user: User) -> None:
        try:
            pass
        except Exception:
            pass