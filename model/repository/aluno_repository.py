from model.connection.mongo_connection import DBConnectionHandler

connection = DBConnectionHandler()
connection.connect_to_db()

class AlunoRepository():
    def __init__(self, db_connection):
        self.collection = db_connection['alunos']
    def add(self, aluno):
        #aluno = {"nome": nome, "email": email, "matricula": matricula, "curso": curso}
        return self.collection.insert_one(aluno).acknowledged

    def get_one(self, matricula):
        aluno = self.collection.find_one({"matricula": matricula}, {"_id": 0})
        return aluno

    def get_many(self, filter):
        alunos = self.collection.find(filter, {"_id": 0})
        return list(alunos)

    def update(self, matricula, alterados):
        aluno = self.get_one(matricula)
        if aluno:
            for chave in alterados.keys():
                if chave in aluno.keys():
                    aluno[chave] = alterados[chave]
        return self.collection.update_one({"matricula": matricula}, {"$set": aluno}).modified_count

    def delete(self, matricula, nome):
        aluno = self.get_one(matricula)
        if aluno['nome'] == nome:
            return self.collection.delete_one({'matricula': matricula}).acknowledged

        return {404, "Aluno não encontrado"}



