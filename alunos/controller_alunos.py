from flask import Blueprint, request, jsonify
from .model_alunos import getAlunos, getAlunoId, createAlunos, updateAluno, deleteAluno
from turmas.model_turmas import getTurmas

alunos_blueprint = Blueprint('alunos', __name__)


@alunos_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    r = request.json
    createAlunos(r)
    return jsonify(r),201
    # r = request.json
    # response = createAlunos(r)  
    # if 'erro' in response:
    #     return jsonify(response), 400  
    # return jsonify(response), 201  


@alunos_blueprint.route('/alunos/<int:idAluno>', methods=['GET'])
def get_aluno(idAluno):
    aluno = getAlunoId(idAluno)
    return jsonify(aluno)
    # aluno = getAlunoId(idAluno)
    # if aluno:
    #     return jsonify(aluno), 200  
    # return jsonify({"erro": "Aluno não encontrado"}), 404  


@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(getAlunos())
    # alunos = getAlunos()
    # return jsonify(alunos), 200  


@alunos_blueprint.route('/alunos/<int:idAluno>', methods=['PUT'])
def update_aluno(idAluno):
    r = request.json
    updateAluno(idAluno, r)
    return jsonify(getAlunoId(idAluno))
    # r = request.json
    # aluno_existe = getAlunoId(idAluno)
    # if not aluno_existe:
    #     return jsonify({"erro": "Aluno não encontrado"}), 404
    # response = updateAluno(idAluno, r)
    # return jsonify(response), 200


@alunos_blueprint.route('/alunos/<int:idAluno>', methods=['DELETE'])
def delete_aluno(idAluno):
    deleteAluno(idAluno)
    return '',204
    # response = deleteAluno(idAluno)
    # if 'erro' in response:
    #     return jsonify(response), 404  
    # return jsonify(response), 200  
