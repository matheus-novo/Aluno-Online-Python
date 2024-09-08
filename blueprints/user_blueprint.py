from flask_login import LoginManager, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from flask import Blueprint, request
from controller.user_controller import UserController
from security.auth import User

user_blueprint = Blueprint('user', __name__)

user_controller = UserController()
loin_manager = LoginManager()

_bcrypt = Bcrypt()


@user_blueprint.route('/login', methods=['POST'])
def login():
    data = dict(request.get_json())
    registro = data['matricula']
    senha = data['senha']

    user_data = user_controller.get_user(registro)

    if user_data and _bcrypt.check_password_hash(user_data['senha'], senha):
        user = User(str(user_data['_id']), user_data['registro'], user_data['senha'], user_data['rule'])
        login_user(user)
        return 'Logado com sucesso'
    return 'Credenciais inválidas'
