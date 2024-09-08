from bson.objectid import ObjectId


class User:
    def __init__(self, db_connection):
        self.collection = db_connection['users']

    def create(self, user_data):
        self.collection.insert_one(user_data)


    def get_user_by_id(self, user_id):
        return self.collection.find_one({'id': ObjectId(user_id)})

    def get_user_by_registro(self, registro):
        return self.collection.find_one({'registro': registro})
