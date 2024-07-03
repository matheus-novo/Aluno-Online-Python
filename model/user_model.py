from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_id, username, password, rules):
        self.id = user_id
        self.username = username
        self.password = password
        self.rules = rules

