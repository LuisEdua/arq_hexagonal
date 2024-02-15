import datetime
import uuid
import bcrypt
from datetime import datetime

class User:
    def __init__(self, name, lastname, cellphone, email, password):
        self.uuid = uuid.uuid4()
        self.name = name
        self.last_name = lastname
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')
        self.cellphone = cellphone
        self.activation_token = str(uuid.uuid4())
        self.activated_at = None

    def to_dict(self, user):
        return {
            "uuid": str(self.uuid),
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "cellphone": self.cellphone,
            "activation_token": self.activation_token,
            "activated_at": str(self.activated_at)
        }
