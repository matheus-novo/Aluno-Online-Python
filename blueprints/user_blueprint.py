from flask_bcrypt import Bcrypt
from flask import Blueprint, request
from controller.user_controller import UserController
from security.required_roles import required_roles
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
        user_role = {"role": user_data['role']}
        access_token = create_access_token(identity=registro, additional_claims=user_role)
        return {'access token': access_token}, 200
    return {"error": "Credenciais inválidas"}, 400


@user_blueprint.route('/teste', methods=['GET'])
@jwt_required()
@required_roles('aluno')
def teste():
    print(get_jwt_identity())
    return 'Logado como aluno'


@user_blueprint.route('/teste2', methods=['GET'])
@jwt_required()
@required_roles('admin')
def teste2():
    print(get_jwt_identity())
    return 'Logado como aluno'



