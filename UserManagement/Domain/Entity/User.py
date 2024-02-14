import uuid
import bcrypt


class User:
    def __init__(self, name, last_name, cellphone, email, password):
        self.uuid = uuid.uuid4()
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')
        self.cellphone = cellphone
        self.activation_token = None
        self.activated_at = None
