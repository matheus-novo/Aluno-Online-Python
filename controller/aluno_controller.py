from model.repository.aluno_repository import AlunoRepository
from model.connection.mongo_connection import DBConnectionHandler

connection_handler = DBConnectionHandler()
connection_handler.connect_to_db()
db_connection = connection_handler.get_db_connection()

class AlunoController:
    def __init__(self, db_connection):
        self.repository = AlunoRepository(db_connection)

    def create_aluno(self, nome, email, matricula, curso):
        aluno = {"nome": nome, "email": email, "matricula": matricula, "curso": curso, "cadeiras": {}}
        self.repository.add(aluno)

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


