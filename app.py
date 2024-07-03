from controller.aluno_controller import AlunoController
from model.connection.mongo_connection import DBConnectionHandler
from flask import Flask, request
from util.verify import Verify

app = Flask('__main__')

connection_handler = DBConnectionHandler()
connection_handler.connect_to_db()
db_connection = connection_handler.get_db_connection()
aluno_controller = AlunoController(db_connection)

verify = Verify()

@app.route('/')
def home():
    return 'Bem vindo!'


@app.route('/aluno/<string:matricula>', methods=['GET'])
def get_aluno_by_matricula(matricula):
    aluno = aluno_controller.get_aluno(matricula=matricula)
    return aluno, 200


@app.route('/aluno', methods=['GET'])
def get_aluno_by_filter():
    body = request.get_json()
    aluno = aluno_controller.get_aluno(filter=body)
    return aluno, 200


@app.route('/course/<string:course_name>', methods=['GET'])
def get_aluno_by_course(course_name):
    filter = {"curso":course_name}
    aluno = aluno_controller.get_aluno(filter=filter)
    return aluno, 200


@app.route('/aluno', methods=['POST'])
def add_aluno():
    aluno = dict(request.get_json())
    print(aluno)
    validate = verify.validate_aluno(aluno)
    print(validate)
    if validate == 200:
        try:
            aluno_controller.add_aluno(aluno)
            return aluno, 200
        except Exception as e:
            return e
    return 'Erradoo'


if __name__ == "__main__":
    app.run(debug=True)
