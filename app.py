from controller.aluno_controller import AlunoController
from model.connection.mongo_connection import DBConnectionHandler
from blueprints.aluno_blueprint import aluno_blueprint
from blueprints.user_blueprint import user_blueprint
from security.auth import init_login_manager
from flask import Flask, request
from util.verify import Verify
from security.config import SECRET_KEY
from flask_bcrypt import Bcrypt

app = Flask('__main__')
app.config['SECRET_KEY'] = SECRET_KEY

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
    init_login_manager(app)
    app.run(debug=True)
