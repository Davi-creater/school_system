from flask import Blueprint, request, jsonify
from .model_turmas import getTurmas, getTurmaId, createTurmas, updateTurma, deleteTurma, info_turmas
from professores.model_professores import getProfessores

turmas_blueprint = Blueprint('turmas',__name__)

@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    r = request.json
    resultado = createTurmas(r)
    if "erro" in resultado:
        return jsonify(resultado), 400
    return jsonify(resultado), 200

@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['PUT'])
def update_turma(idTurma):
     r = request.json
     turma_existe = getTurmaId(idTurma)
     if not turma_existe:
          return jsonify({"error":"turma nao encontrado"})
     update = updateTurma(idTurma,r)
     return jsonify(update), 200


@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['DELETE'])
def delete_turma(idTurma):
     delete = deleteTurma(idTurma)
     return jsonify(delete), 200

@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['GET'])
def getTurmaId(idTurma):
    turma = getTurmaId(idTurma)
    if turma:
        return jsonify(turma), 200
    return jsonify({"erro": "Turma não encontrada"}), 404

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
     return jsonify(getTurmas())