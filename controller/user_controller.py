from model.connection.mongo_connection import DBConnectionHandler
from model.repository.user_repository import User
from security.pass_generator import PasswordGenerator
from flask_bcrypt import Bcrypt

connection_handler = DBConnectionHandler()
connection_handler.connect_to_db()
db_connection = connection_handler.get_db_connection()

password_generator = PasswordGenerator()

_bcrypt = Bcrypt()

user_repository = User(db_connection)


class UserController:
    def __init__(self):
        pass

    def create_user(self, registro, role):
        try:
            senha_temp = password_generator.gerar(6)
        except:
            senha_temp = "Senha@123"

        senha_temp_hash = _bcrypt.generate_password_hash(senha_temp).decode('utf-8')

        user = {'registro': registro, 'senha': senha_temp_hash, 'role': role}

        print(senha_temp)
        print(senha_temp_hash)

        try:
            user_repository.create(user)
            return senha_temp
        except Exception as e:
            print(e)
            return None

    def get_user(self, registro):
        return user_repository.get_user_by_registro(registro)


    def get_by_id(self, user_id):
        return user_repository.get_user_by_id(user_id)

