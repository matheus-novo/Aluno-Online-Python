from flask import Blueprint, request
from controller.aluno_controller import AlunoController
from model.connection.mongo_connection import DBConnectionHandler
from flask_login import login_required

connection_handler = DBConnectionHandler()
connection_handler.connect_to_db()
db_connection = connection_handler.get_db_connection()

aluno_controller = AlunoController(db_connection)

aluno_blueprint = Blueprint('aluno', __name__)

@aluno_blueprint.route('/aluno/<string:matricula>', methods=['GET'])
def get_aluno_by_matricula(matricula):
    aluno = aluno_controller.get_aluno(matricula=matricula)
    print(aluno)
    return aluno, 200


@aluno_blueprint.route('/aluno', methods=['GET'])
@login_required
def get_aluno_by_filter():
    body = request.get_json()
    aluno = aluno_controller.get_aluno(filter=body)
    return aluno, 200


@aluno_blueprint.route('/course/<string:course_name>', methods=['GET'])
def get_aluno_by_course(course_name):
    filter = {"curso":course_name}
    aluno = aluno_controller.get_aluno(filter=filter)
    return aluno, 200


@aluno_blueprint.route('/aluno', methods=['POST'])
def add_aluno():
    #aluno = request.form.to_dict()
    aluno = dict(request.get_json())
    #print(aluno)
    return aluno_controller.create_aluno(aluno)
    #validate = verify.validate_aluno(aluno)
    #print(validate)
    #if validate == 200:
    #return 'Erradoo'


