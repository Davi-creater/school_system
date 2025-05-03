from flask import Blueprint, request, jsonify
from .model_professores import getProfessores, getProfessorId, createProfessor, updateProfessor, deleteProfessor

professores_blueprint = Blueprint('professores', __name__)  

# Rota para criar um professor
@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    r = request.json
    if not r.get('nome'):
        return jsonify({"erro": "o campo 'nome' é obrigatório"}), 400
    # Cria o professor no banco
    createProfessor(r)
    return jsonify({"mensagem": "Professor criado com sucesso", "professor": r}), 201  

# Rota para atualizar um professor
@professores_blueprint.route('/professores/<int:idProfessor>', methods=['PUT'])
def update_professor(idProfessor):
    r = request.json
    # Verifica se o professor existe
    professor_existe = getProfessorId(idProfessor)
    if not professor_existe:
        return jsonify({"error": "professor não encontrado"}), 404  
    # Atualiza o professor
    updateProfessor(idProfessor, r)
    return jsonify({"mensagem": "Professor atualizado com sucesso", "professor": getProfessorId(idProfessor)}), 200  

# Rota para deletar um professor
@professores_blueprint.route('/professores/<int:idProfessor>', methods=['DELETE'])
def delete_professor(idProfessor):
    # Verifica se o professor existe antes de tentar deletá-lo
    professor_existe = getProfessorId(idProfessor)
    if not professor_existe:
        return jsonify({"error": "professor não encontrado"}), 404
    deleteProfessor(idProfessor)
    return '', 204  # Deleção bem-sucedida, sem conteúdo

# Rota para obter um professor específico
@professores_blueprint.route('/professores/<int:idProfessor>', methods=['GET'])
def get_professor(idProfessor):
    professor = getProfessorId(idProfessor)
    if not professor:
        return jsonify({"error": "professor não encontrado"}), 404  
    return jsonify(professor), 200

# Rota para obter todos os professores
@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(getProfessores()), 200  
