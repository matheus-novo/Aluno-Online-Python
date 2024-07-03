
class User():
    def __init__(self, db_connection):
        self.collection = db_connection['users']

    def create(self, user_data):
        try:
            self.collection.insert_one(user_data)
        except Exception as e:
            return e





