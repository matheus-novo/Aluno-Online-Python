from model.connection.mongo_connection import DBConnectionHandler

connection = DBConnectionHandler()
connection.connect_to_db()


class AlunoRepository:
    def __init__(self, db_connection):
        self.collection = db_connection['alunos']

    def add(self, aluno):
        return self.collection.insert_one(aluno).acknowledged

    def get_one(self, matricula):
        aluno = self.collection.find_one({"matricula": matricula}, {"_id": 0})
        return aluno

    def get_many(self, filter):
        alunos = self.collection.find(filter, {"_id": 0})
        return list(alunos)

    def update(self, matricula, updated_aluno):
        return self.collection.update_one({"matricula": matricula}, {"$set": updated_aluno}).modified_count

    def delete(self, matricula):
        return self.collection.delete_one({'matricula': matricula}).acknowledged
