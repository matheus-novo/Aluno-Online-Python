from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_id, register, password):
        self.id = user_id
        self.register = register
        self.password = password
        #self.rule = rule

