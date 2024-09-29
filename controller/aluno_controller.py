from model.repository.aluno_repository import AlunoRepository
from model.connection.mongo_connection import DBConnectionHandler
from controller.user_controller import UserController
from flask_bcrypt import Bcrypt

connection_handler = DBConnectionHandler()
connection_handler.connect_to_db()
db_connection = connection_handler.get_db_connection()

user_contoller = UserController()

_bcrypt = Bcrypt()

class AlunoController:
    def __init__(self, db_connection):
        self.repository = AlunoRepository(db_connection)

    def create_aluno(self, aluno_request):
        nome = aluno_request["nome"]
        email = aluno_request["email"]
        matricula = aluno_request["matricula"]
        curso = aluno_request["curso"]

        if self.repository.get_one(matricula) != None:
            aluno = {"nome": nome, "email": email, "matricula": matricula, "curso": curso, "cadeiras": {}}
            if self.repository.add(aluno):
                senha_temporaria = user_contoller.create_user(matricula, 'aluno')
                return {'Senha Temporária': senha_temporaria}, 201
            return {400: "BAD REQUEST"}

    def add_aluno(self, aluno):
        return self.repository.add(aluno)

    def get_aluno(self, matricula=None, filter=None):
        if matricula:
            return self.repository.get_one(matricula)
        elif filter:
            return self.repository.get_many(filter)
        else:
            return None

    def get_media(self, matricula, cadeira):
        aluno = self.repository.get_one(matricula)
        if aluno and cadeira in aluno['cadeiras'].keys():
            soma = 0
            for nota in aluno['cadeiras'][cadeira]:
                soma += nota
            media = soma / len(aluno['cadeiras'][cadeira])
            return media
        return 'Not Found'

    def add_nota(self, matricula, cadeira, nota):
        aluno = self.repository.get_one(matricula)
        aluno['cadeiras'][cadeira].append(nota)
        modificados = self.repository.update(matricula, aluno)
        print(modificados)


