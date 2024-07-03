from model.connection.mongo_credencials import MONGO_USER, MONGO_SERVER, MONGO_PASSWORD, MONGO_DATABASE
from pymongo import MongoClient


class DBConnectionHandler():
    def __init__(self):
        self.connection_string = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_SERVER}"
        self.client = ''
        self.connection = ''

    def connect_to_db(self):
        self.client = MongoClient(self.connection_string)
        self.connection = self.client[MONGO_DATABASE]

    def get_db_connection(self):
        return self.connection
