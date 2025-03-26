from flask import Flask, request, jsonify

app = Flask(__name__)

info_alunos = {
    "alunos": [
        {
            "id": 1,
            "turma_id": 1,
            "nome": "Davi",
            "data_nascimento": "21/09/2005",
            "nota_primeiro_semestre": "10",
            "nota_segundo_sementre": "10",
        }
    ]
}

info_professores = {
    "professores": [
        {
            "id": 1,
            "nome": "Professor Teste",
            "data_nascimento": "12/04/1992",
            "disciplina": "Matemática",
            "salario": "1500",
        }
    ]
}

info_turmas = {
    "turmas": [
        {
            "id": 1,
            "nome": "Turma A",
            "turno": "Matutino",
            "professor_id": 1,
            "ativo": True
        }
    ]
}


# -----------------------------------POST------------------------------------
@app.route("/alunos", methods=["POST"])
def createAlunos():
    r = request.json
    turma_id = r.get("turma_id")
    if not turma_id:
        return jsonify({"error": "ID da turma é obrigatório"}), 400

    turmas = info_turmas["turmas"]
    turma_existe = any(turma["id"] == turma_id for turma in turmas)
    if not turma_existe:
        return jsonify({"error": "Turma não encontrada"}), 404

    aluno = info_alunos["alunos"]
    aluno.append(r)
    return jsonify(r), 201


@app.route("/professores", methods=["POST"])
def createProfessores():
    r = request.json
    professor = info_professores["professores"]
    professor.append(r)
    return jsonify(r), 201


@app.route("/turmas", methods=["POST"])
def createTurma():
    r = request.json
    professor_id = r.get("professor_id")
    if not professor_id:
        return jsonify({"error": "ID do professor é obrigatório"}), 400

    professores = info_professores["professores"]
    professor_existe = any(
        professor["id"] == professor_id for professor in professores
    )
    if not professor_existe:
        return jsonify({"error": "Professor não encontrado"}), 404

    turma = info_turmas["turmas"]
    turma.append(r)
    return jsonify(r), 201


# -----------------------------------POST------------------------------------
# -----------------------------------PUT------------------------------------
@app.route("/alunos/<int:idAluno>", methods=["PUT"])
def updateAluno(idAluno):
    alunos = info_alunos["alunos"]
    for aluno in alunos:
        if aluno["id"] == idAluno:
            r = request.json
            if "nome" in r:
                aluno["nome"] = r["nome"]
            if "idade" in r:
                aluno["idade"] = r["idade"]
            if "data_nascimento" in r:
                aluno["data_nascimento"] = r["data_nascimento"]
            if "nota_primeiro_semestre" in r:
                aluno["nota_primeiro_semestre"] = r["nota_primeiro_semestre"]
            if "nota_segundo_semestre" in r:
                aluno["nota_segundo_semestre"] = r["nota_segundo_semestre"]

            return jsonify(r), 200

    return jsonify({"error": "Aluno não encontrado"}), 404


@app.route("/professores/<int:idProfessor>", methods=["PUT"])
def updateProfessor(idProfessor):
    professores = info_professores["professores"]
    for professor in professores:
        if professor["id"] == idProfessor:
            r = request.json
            if "nome" in r:
                professor["nome"] = r["nome"]
            if "idade" in r:
                professor["idade"] = r["idade"]
            if "materia" in r:
                professor["materia"] = r["materia"]
            if "observacoes" in r:
                professor["observacoes"] = r["observacoes"]
            return jsonify(r), 200

    return jsonify({"error": "Professor não encontrado"}), 404


@app.route("/turmas/<int:idTurma>", methods=["PUT"])
def updateTurma(idTurma):
    turmas = info_turmas["turmas"]
    for turma in turmas:
        if turma["id"] == idTurma:
            r = request.json
            if "descricao" in r:
                turma["descricao"] = r["descricao"]
            if "ativo" in r:
                turma["ativo"] = r["ativo"]
            return jsonify(r), 200

    return jsonify({"error": "Turma não encontrada"}), 404


# -----------------------------------PUT------------------------------------


# -----------------------------------GET------------------------------------
@app.route("/alunos", methods=["GET"])
def getAlunos():
    dados = info_alunos["alunos"]
    return jsonify(dados), 200


@app.route("/alunos/<int:idAluno>", methods=["GET"])
def getAlunoId(idAluno):
    alunos = info_alunos["alunos"]
    for aluno in alunos:
        if aluno["id"] == idAluno:
            return jsonify(aluno), 200
    return jsonify({"error": "Aluno não encontrado"}), 404


@app.route("/professores", methods=["GET"])
def getProfessores():
    dados = info_professores["professores"]
    return jsonify(dados), 200


@app.route("/professores/<int:idProfessor>", methods=["GET"])
def getProfessorId(idProfessor):
    professores = info_professores["professores"]
    for professor in professores:
        if professor["id"] == idProfessor:
            return jsonify(professor), 200
    return jsonify({"error": "Professor não encontrado"}), 404


@app.route("/turmas", methods=["GET"])
def getTurmas():
    dados = info_turmas["turmas"]
    return jsonify(dados), 200


@app.route("/turmas/<int:idTurma>", methods=["GET"])
def getTurmaId(idTurma):
    turmas = info_turmas["turmas"]
    for turma in turmas:
        if turma["id"] == idTurma:
            return jsonify(turma), 200
    return jsonify({"error": "Turma não encontrada"}), 404


# -----------------------------------GET------------------------------------

# -----------------------------------DELETE------------------------------------


@app.route("/alunos/<int:idAluno>", methods=["DELETE"])
def deleteAluno(idAluno):
    alunos = info_alunos["alunos"]
    for aluno in alunos:
        if aluno["id"] == idAluno:
            alunos.remove(aluno)
            return jsonify({"REMOVIDO": aluno}), 200
    return jsonify({"error": "Aluno não encontrado"}), 404


@app.route("/professores/<int:idProfessor>", methods=["DELETE"])
def deleteProfessor(idProfessor):
    professores = info_professores["professores"]
    for professor in professores:
        if professor["id"] == idProfessor:
            professores.remove(professor)
            return jsonify({"REMOVIDO": professor}), 200
    return jsonify({"error": "Professor não encontrado"}), 404


@app.route("/turmas/<int:idTurma>", methods=["DELETE"])
def deleteTurma(idTurma):
    turmas = info_turmas["turmas"]
    for turma in turmas:
        if turma["id"] == idTurma:
            turmas.remove(turma)
            return jsonify({"REMOVIDO": turma}), 200
    return jsonify({"error": "Turma não encontrada"}), 404


# -----------------------------------DELETE------------------------------------


if __name__ == "__main__":
    app.run(debug=True)