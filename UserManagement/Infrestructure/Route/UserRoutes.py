from flask import Blueprint, request
from UserManagement.Infrestructure.Controller.RegisterUserController import RegisterUserController
from UserManagement.Application.UseCase.RegisterUserUseCase import RegisterUserUseCase
from UserManagement.Infrestructure.Repository.UserMySQLRepository import UserMySQLRepository
from UserManagement.Infrestructure.Controller.ActivateUserController import ActivateUserController
from UserManagement.Application.UseCase.ActivateUserUseCase import ActivateUserUseCase
#from UserManagement.Infrestructure.Repository.UserMongoDBRepository import UserMongoDBRepository
from UserManagement.Infrestructure.Repository.Models.UserMySQLModel import User
#from UserManagement.Infrestructure.Repository.Models.UserMongoDBModel import User


user_blueprint = Blueprint('users', __name__)
#repository = UserMongoDBRepository()
repository = UserMySQLRepository()
registerUserCase = RegisterUserUseCase(repository)
registerUserController = RegisterUserController(registerUserCase)
activateUserCase = ActivateUserUseCase(repository)
activateUserController = ActivateUserController(activateUserCase)

@user_blueprint.route('/', methods=['POST'])
def register_user():
    data = request.get_json()
    return registerUserController.run(data)

@user_blueprint.route('/<activation_token>/active', methods=['PUT'])
def activate_user(activation_token):
    return activateUserController.run(activation_token)