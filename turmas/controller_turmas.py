from flask import Blueprint, request, jsonify
from .model_turmas import getTurmas, getTurmaId, createTurmas, updateTurma,deleteTurma
from professores.model_professores import getProfessores

turmas_blueprint = Blueprint('turmas',__name__)

@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
        r = request.json
        #professores = getProfessores()
       # if "nome" not in r or not r["nome"].strip():
         #   return jsonify({"erro":"o campo nao foi preenchido"})
        #if "professor_id" not in r:
           # return jsonify({"erro":"error ao criar"})
        create = createTurmas(r)
        return jsonify(create)

@turmas_blueprint.route('/turmas<int:idTurma>', methods=['PUT'])
def update_turma(idTurma):
     r = request.json
     turma_existe = getTurmaId(idTurma)
     if not turma_existe:
          return jsonify({"error":"turma nao encontrado"})
     update = updateTurma(idTurma,r)
     return jsonify(update)


@turmas_blueprint.route('/turmas<int:idTurma>', methods=['DELETE'])
def delete_turma(idTurma):
     delete = deleteTurma(idTurma)
     return jsonify(delete)

@turmas_blueprint.route('/turmas<int:idTurma>', methods=['GET'])
def get_turma(idTurma):
     turma = getTurmaId(idTurma)
     return jsonify(turma)

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
     return jsonify(getTurmas())