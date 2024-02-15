from UserManagement.Application.UseCase.RegisterUserUseCase import RegisterUserUseCase
from flask import jsonify
from UserManagement.Infrestructure.Service.Email import Email

class RegisterUserController:

    def __init__(self, registerUserUseCase: RegisterUserUseCase):
        self.registerUserUseCase = registerUserUseCase

    def run(self, user_data):
        try:
            name = user_data.get("name")
            last_name = user_data.get("last_name")
            email = user_data.get("email")
            password = user_data.get("password")
            cellphone = user_data.get("cellphone")
            user = self.registerUserUseCase.run(name, last_name, cellphone, email, password)
            Email().run(user)
            return jsonify({"mesage": "User created", "Codigo": 201}), 201
        except Exception as e:
            return jsonify({"Error": str(e), "Codigo": 500}), 500
