from UserManagement.Application.UseCase.ActivateUserUseCase import ActivateUserUseCase
from flask import jsonify


class ActivateUserController:
    def __init__(self, use_case: ActivateUserUseCase):
        self._use_case = use_case

    def run(self, activation_token):
        try:
            user = self._use_case.run(activation_token)
            return jsonify({"message": "User Validated", "Codigo": 201, "user": user}), 201
        except Exception as e:
            return jsonify({"Error": str(e), "Codigo": 500}), 500
