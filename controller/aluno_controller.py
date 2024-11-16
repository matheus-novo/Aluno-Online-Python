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

        if self.repository.get_one(matricula) is not None:
            return {"error": "Matricula já existe"}, 400

        aluno = {"nome": nome, "email": email, "matricula": matricula, "curso": curso, "cadeiras_matriculadas": {}}
        if self.repository.add(aluno):
            senha_temporaria = user_contoller.create_user(matricula, 'aluno')
            return {"message": "Aluno criado com sucesso", "Senha Temporária": senha_temporaria}, 201

        return {"error": "Erro ao criar aluno"}, 400

    def add_aluno(self, aluno):
        return self.repository.add(aluno)

    def get_aluno(self, matricula=None, filter=None):
        if matricula:
            aluno = self.repository.get_one(matricula)
            return aluno, 200
        elif filter:
            alunos = self.repository.get_many(filter)
            return alunos, 200
        else:
            return {"error": "Aluno não encontrado"}, 404

    def update_aluno(self, matricula, new_data):
        aluno = self.repository.get_one(matricula)

        if not aluno:
            return {"error": "Não encontrado"}, 404

        for chave in new_data.keys():
            if chave in aluno.keys():
                aluno[chave] = new_data[chave]
        if self.repository.update(matricula, aluno) > 0:
            return {"message": "Atualizado"}, 200

        return {"error": "Nenhum item alterado"}, 400

    def delete_aluno(self, matricula, nome):
        aluno = self.repository.get_one(matricula)

        if not aluno:
            return {"error": "Aluno não encontrado"}, 404

        if aluno['nome'] is not nome:
            return {"error": "Nome não confere"}, 400

        if self.repository.delete(matricula):
            return {"message": "Aluno deletado com sucesso"}, 200

        return {"error": "Erro ao deletar"}, 400


    def add_cadeira(self, matricula, nome_cadeira):
        aluno = self.repository.get_one(matricula)

        if not aluno:
            return {"error": "Aluno não encontrado"}, 404

        if nome_cadeira in aluno['cadeiras'].keys():
            return {"error": "Aluno já está matriculado nessa cadeira"}, 400

        aluno['cadeiras'][nome_cadeira] = []

        modificados = self.repository.update(matricula, aluno)

        if modificados > 0:
            return {"message": "Cadeira adicionada com sucesso"}, 200

        return {"error": "Não foi possível adicionar cadeira"}, 400

    def get_media(self, matricula, cadeira):
        aluno = self.repository.get_one(matricula)

        if not aluno:
            return {"error": "Aluno não encontrado"}, 404

        if cadeira not in aluno['cadeiras'].keys():
            return {"error": "Cadeira não encontrada"}, 404

        soma = 0
        for nota in aluno['cadeiras'][cadeira]:
            soma += nota
        media = soma / len(aluno['cadeiras'][cadeira])
        return {"media": media}, 200

    def add_nota(self, matricula, cadeira, nota):
        aluno = self.repository.get_one(matricula)

        if not aluno:
            return {"error": "Aluno não encontrado"}, 404

        if cadeira not in aluno.keys():
            return {"error": "Cadeira não encontrada"}, 404

        aluno['cadeiras'][cadeira].append(nota)

        modificados = self.repository.update(matricula, aluno)

        if modificados > 0:
            return {"message": "Nota adicionada com sucesso"}, 200

        return {"error": "Não foi possível adicionar nota"}, 400
