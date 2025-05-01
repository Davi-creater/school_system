from flask import Blueprint, request, jsonify
from .model_professores import getProfessores, getProfessorId, createProfessor, updateProfessor, deleteProfessor

professores_blueprint = Blueprint('professores', __name__)  

@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    r = request.json
    createProfessor(r)
    return jsonify(r),201
    # if not r.get('nome'):
    #     return jsonify({"erro": "o campo 'nome' é obrigatório"}), 400
    # create = createProfessor(r)
    # return jsonify(create), 201  

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['PUT'])
def update_professor(idProfessor):
    r = request.json
    updateProfessor(idProfessor, r)
    return jsonify(getProfessorId(idProfessor))
    # professor_existe = getProfessorId(idProfessor)
    # if not professor_existe:
    #     return jsonify({"error": "professor não encontrado"}), 404  
    # update = updateProfessor(idProfessor, r)
    # return jsonify(update), 200  

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['DELETE'])
def delete_professor(idProfessor):
    deleteProfessor(idProfessor)
    # delete = deleteProfessor(idProfessor)
    # return jsonify(delete), 200  

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['GET'])
def get_professor(idProfessor):
    professor = getProfessorId(idProfessor)
    if not professor:
        return jsonify({"error": "professor não encontrado"}), 404  
    return jsonify(professor), 200  

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(getProfessores()), 200  
from flask import Blueprint, request, jsonify
from .model_professores import getProfessores, getProfessorId, createProfessor, updateProfessor, deleteProfessor

professores_blueprint = Blueprint('professores', __name__)  

@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    r = request.json
    if not r.get('nome'):
        return jsonify({"erro": "o campo 'nome' é obrigatório"}), 400
    create = createProfessor(r)
    return jsonify(create), 201  

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['PUT'])
def update_professor(idProfessor):
    r = request.json
    professor_existe = getProfessorId(idProfessor)
    if not professor_existe:
        return jsonify({"error": "professor não encontrado"}), 404  
    update = updateProfessor(idProfessor, r)
    return jsonify(update), 200  

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['DELETE'])
def delete_professor(idProfessor):
    delete = deleteProfessor(idProfessor)
    return "", 204

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['GET'])
def get_professor(idProfessor):
    professor = getProfessorId(idProfessor)
    return jsonify(professor)

    # professor = getProfessorId(idProfessor)
    # if not professor:
    #     return jsonify({"error": "professor não encontrado"}), 404  
    # return jsonify(professor), 200  

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(getProfessores()), 200  
