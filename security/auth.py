from flask_login import LoginManager
from model.user_model import User
from controller.user_controller import UserController

login_manager = LoginManager()


def init_login_manager(app):
    login_manager.init_app(app)

    user_controller = UserController()

    @login_manager.user_loader
    def load_user(user_id):
        user_data = user_controller.get_by_id(user_id)
        if user_data:
            return User(
                str(user_data['_id']),
                user_data['username'],
                user_data['password'],
                user_data['rules']
            )
        return None