from flask import Blueprint, request, jsonify
from .model_alunos import getAlunos, getAlunoId, createAlunos, updateAluno,deleteAluno
from turmas.model_turmas import getTurmaId, getTurmas

alunos_blueprint = Blueprint('alunos',__name__)

@alunos_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
        r = request.json
        turmas = getTurmas()
        if "nome" not in r or not r["nome"].strip():
            return jsonify({"erro":"o campo nao foi preenchido"})
        if "turma_id" not in r:
            return jsonify({"erro":"error ao criar"})
        create = createAlunos(r, turmas)
        return jsonify(create)

@alunos_blueprint.route('/alunos<int:idAluno>', methods=['PUT'])
def update_aluno(idAluno):
     r = request.json
     aluno_existe = getAlunoId(idAluno)
     if not aluno_existe:
          return jsonify({"error":"aluno nao encontrado"})
     update = updateAluno(idAluno,r)
     return jsonify(update)


@alunos_blueprint.route('/alunos<int:idAluno>', methods=['DELETE'])
def delete_aluno(idAluno):
     delete = deleteAluno(idAluno)
     return jsonify(delete)

@alunos_blueprint.route('/alunos<int:idAluno>', methods=['GET'])
def get_aluno(idAluno):
     aluno = getAlunoId(idAluno)
     return jsonify(aluno)

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
     return jsonify(getAlunos())