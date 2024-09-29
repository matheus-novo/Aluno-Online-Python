from flask_bcrypt import Bcrypt
from flask import Blueprint, request
from controller.user_controller import UserController
from security.required_rules import required_rules
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt

user_blueprint = Blueprint('user', __name__)

user_controller = UserController()

_bcrypt = Bcrypt()


@user_blueprint.route('/login', methods=['POST'])
def login():
    data = dict(request.get_json())
    registro = data['matricula']
    senha = data['senha']

    user_data = user_controller.get_user(registro)

    if user_data and _bcrypt.check_password_hash(user_data['senha'], senha):
        access_token = create_access_token(identity=registro)
        return {'access token': access_token}
    return 'Credenciais inválidas'


@user_blueprint.route('/teste', methods=['GET'])
@jwt_required()
@required_rules('aluno')
def teste():
    print(get_jwt_identity())
    return 'Logado como aluno'


@user_blueprint.route('/teste2', methods=['GET'])
@jwt_required()
@required_rules('admin')
def teste2():
    print(get_jwt_identity())
    return 'Logado como aluno'



