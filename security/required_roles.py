from flask_jwt_extended import get_jwt_identity
from controller.user_controller import UserController

from functools import wraps

user_controller = UserController()


def required_roles(role_list):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            current_user = user_controller.get_user(get_jwt_identity())
            user_role = current_user['role']
            if user_role not in role_list:
                return {"error": "Acesso não autorizado"}, 401
            return f(*args, **kwargs)
        return wrapped
    return decorator


