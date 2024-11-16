from model.repository.professor_repository import ProfessorRepository
from model.connection.mongo_connection import DBConnectionHandler
from controller.user_controller import UserController
from flask_bcrypt import Bcrypt

connection_handler = DBConnectionHandler()
connection_handler.connect_to_db()
db_connection = connection_handler.get_db_connection()

user_contoller = UserController()

_bcrypt = Bcrypt()


class ProfessorController:
    def __init__(self, db_connection):
        self.repository = ProfessorRepository(db_connection)

    def create_professor(self, professor_request):
        nome = professor_request["nome"]
        email = professor_request["email"]
        matricula = professor_request["matricula"]
        curso = professor_request["curso"]

        if self.repository.get_one(matricula) is not None:
            return {"error": "Matricula já existe"}, 400

        professor = {"nome": nome, "email": email, "matricula": matricula, "cadeiras_ministradas": []}
        if self.repository.add(professor):
            senha_temporaria = user_contoller.create_user(matricula, 'professor')
            return {"message": "Professor criado com sucesso", "Senha Temporária": senha_temporaria}, 201

        return {"error": "Erro ao criar Professor"}, 400

    def get_professor(self, matricula=None, filter=None):
        if matricula:
            professor = self.repository.get_one(matricula)
            return professor, 200
        elif filter:
            professores = self.repository.get_many(filter)
            return professores, 200
        else:
            return {"error": "Professor não encontrado"}, 404

    def update_professor(self, matricula, new_data):
        professor = self.repository.get_one(matricula)

        if not professor:
            return {"error": "Professor não encontrado"}, 404

        for chave in new_data.keys():
            if chave in professor.keys():
                professor[chave] = new_data[chave]
        if self.repository.update(matricula, professor) > 0:
            return {"message": "Atualizado"}, 200

        return {"error": "Nenhum item alterado"}, 400

    def delete_professor(self, matricula, nome):
        professor = self.repository.get_one(matricula)

        if not professor:
            return {"error": "Professor não encontrado"}, 404

        if professor['nome'] is not nome:
            return {"error": "Nome não confere"}, 400

        if self.repository.delete(matricula):
            return {"message": "Professor deletado com sucesso"}, 200

        return {"error": "Erro ao deletar"}, 400

