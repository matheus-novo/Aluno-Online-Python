from controller.aluno_controller import AlunoController
from model.connection.mongo_connection import DBConnectionHandler
from blueprints.aluno_blueprint import aluno_blueprint
from blueprints.user_blueprint import user_blueprint
from security.auth import login_manager
from flask import Flask
from util.verify import Verify
from security.config import SECRET_KEY, JWT_SECRET_KEY
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask('__main__')
app.config['SECRET_KEY'] = SECRET_KEY
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

jwt_manager = JWTManager()

login_manager.init_app(app)

app.register_blueprint(aluno_blueprint)
app.register_blueprint(user_blueprint)

_bcrypt = Bcrypt(app)

connection_handler = DBConnectionHandler()
connection_handler.connect_to_db()
db_connection = connection_handler.get_db_connection()
aluno_controller = AlunoController(db_connection)

verify = Verify()

@app.route('/')
def home():
    return 'Bem vindo!'


if __name__ == "__main__":
    jwt_manager.init_app(app)
    app.run(debug=True)
