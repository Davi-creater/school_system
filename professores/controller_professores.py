from flask import Blueprint, request, jsonify
from .model_professores import getProfessores, getProfessorId, createProfessor, updateProfessor,deleteProfessor

professores_blueprint = Blueprint('profeessores',__name__)

@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    r = request.json
    create = createProfessor(r)
    return jsonify(create), 201  # <- status correto

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['PUT'])
def update_professor(idProfessor):
     r = request.json
     professor_existe = getProfessorId(idProfessor)
     if not professor_existe:
          return jsonify({"error":"professor nao encontrado"})
     update = updateProfessor(idProfessor,r)
     return jsonify(update)


@professores_blueprint.route('/professores/<int:idProfessor>', methods=['DELETE'])
def delete_professore(idProfessor):
     delete = deleteProfessor(idProfessor)
     return jsonify(delete)

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['GET'])
def get_Professor(idProfessor):
     professor = getProfessorId(idProfessor)
     return jsonify(professor)

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
     return jsonify(getProfessores())