from flask import Blueprint, request, jsonify
from .model_turmas import (
    getTurmas,
    getTurmaId,
    createTurmas,
    updateTurma,
    deleteTurma
)

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route('/turmas', methods=['POST'])
def criar_turma():
    dados = request.json
    nova_turma = {
        'id': dados['id'],
        'nome': dados.get('nome', ''),
        'turno': dados.get('turno', ''),
        'professor_id': dados['professor_id'],
        'ativo': dados.get('ativo', True),
        'descricao': dados.get('descricao', '')
    }
    createTurmas(nova_turma)
    return jsonify(nova_turma), 201

@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['PUT'])
def update_turma(idTurma):
    r = request.json
    turma_existe = getTurmaId(idTurma)
    if not turma_existe:
        return jsonify({"error": "turma nao encontrada"}), 404
    update = updateTurma(idTurma, r)
    return jsonify(update), 200

@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['DELETE'])
def delete_turma(idTurma):
    delete = deleteTurma(idTurma)
    return jsonify(delete), 200

@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['GET'])
def get_turma_por_id(idTurma):
    turma = getTurmaId(idTurma)
    if turma:
        return jsonify(turma), 200
    return jsonify({"erro": "Turma não encontrada"}), 404

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(getTurmas())
