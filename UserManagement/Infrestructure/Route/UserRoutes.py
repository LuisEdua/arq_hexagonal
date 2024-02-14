from flask import Blueprint, request
from UserManagement.Infrestructure.Controller.RegisterUserController import RegisterUserController

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/', methods=['POST'])
def register_user():
    data = request.get_json()
    return RegisterUserController.run(data)
