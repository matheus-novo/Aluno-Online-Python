from model.connection.mongo_connection import DBConnectionHandler

connection = DBConnectionHandler()
connection.connect_to_db()


class ProfessorRepository():
    def __init__(self, db_connection):
        self.collection = db_connection['professores']

    def add(self, professor):
        return self.collection.insert_one(professor).acknowledged

    def get_one(self, matricula):
        professor = self.collection.find_one({"matricula": matricula}, {"_id": 0})
        return professor

    def get_many(self, filter):
        professores = self.collection.find(filter, {"_id": 0})
        return list(professores)

    def update(self, matricula, updated_professor):
        return self.collection.update_one({"matricula": matricula}, {"$set": updated_professor}).modified_count

    def delete(self, matricula):
        return self.collection.delete_one({'matricula': matricula}).acknowledged
