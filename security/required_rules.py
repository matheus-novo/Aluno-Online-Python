from flask_jwt_extended import get_jwt_identity
from controller.user_controller import UserController

from functools import wraps

user_controller = UserController()


def required_rules(rule_list):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            current_user = user_controller.get_user(get_jwt_identity())
            user_rule = current_user['rule']
            if user_rule not in rule_list:
                return 'Unauthorized', 401
            return f(*args, **kwargs)
        return wrapped
    return decorator


