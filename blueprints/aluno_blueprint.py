from flask import Blueprint, request
from controller.aluno_controller import AlunoController
from model.connection.mongo_connection import DBConnectionHandler
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from security.required_roles import required_roles

connection_handler = DBConnectionHandler()
connection_handler.connect_to_db()
db_connection = connection_handler.get_db_connection()

aluno_controller = AlunoController(db_connection)

aluno_blueprint = Blueprint('alunos', __name__, url_prefix='/alunos')


# ROTA DE TESTES
@aluno_blueprint.route('/teste', methods=['GET'])
@jwt_required()
# @required_roles(['admin'])
def testes():
    print(get_jwt()['role'])
    return get_jwt()['role']


@aluno_blueprint.route('/<string:matricula>', methods=['GET'])
@jwt_required()
@required_roles(['aluno', 'professor', 'admin'])
def get_aluno_by_matricula(matricula):
    current_role = get_jwt()['role']
    if current_role == "aluno":
        if get_jwt_identity() != matricula:
            return {"error": "Não autorizado"}, 401
    aluno = aluno_controller.get_aluno(matricula=matricula)
    return {aluno, 200}


@aluno_blueprint.route('/', methods=['GET'])
@jwt_required()
@required_roles(['professor'])
def get_aluno_by_filter():
    body = request.get_json()
    aluno = aluno_controller.get_aluno(filter=body)
    return aluno, 200


@aluno_blueprint.route('/course/<string:course_name>', methods=['GET'])
@jwt_required()
@required_roles(['professor', 'admin'])
def get_aluno_by_course(course_name):
    filter = {"curso": course_name}
    aluno = aluno_controller.get_aluno(filter=filter)
    return aluno, 200


@aluno_blueprint.route('/', methods=['POST'])
@jwt_required()
# @required_roles(['admin'])
def add_aluno():
    aluno = dict(request.get_json())
    return aluno_controller.create_aluno(aluno)


@aluno_blueprint.route('/<string:matricula>/notas')
@jwt_required()
@required_roles(['aluno'])
def show_notas(matricula):
    if matricula != get_jwt_identity():
        return 'UNAUTHORIZED', 401

    aluno = aluno_controller.get_aluno(matricula=matricula)
    return aluno['cadeiras']
