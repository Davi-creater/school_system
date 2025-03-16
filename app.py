from flask import Flask, request, jsonify

app = Flask(__name__)

info_alunos = {
    "alunos":[
        {"id": 1,
         "nome":"Davi",
         "idade":"19",
         "turma_id":"1",
         "data_nascimento":"21/09/2005",
         "nota_primeiro_semestre":"10",
         "nota_segundo_sementre":"10",
         "media_final":"10"
        }
    ]
}

info_professores = {
    "professores":[
        {"id": 1,
         "nome":"",
         "idade":"",
         "materia":"",
         "observacoes":"",
        }
    ]
}

info_turmas = {
    "turmas":[
        {"id": 1,
         "descricao":"",
         "professor_id":"",
         "ativo":"",
        }
    ]
}
#-----------------------------------POST------------------------------------
@app.route('/alunos', methods=['POST'])
def createAlunos():
    r = request.json
    aluno = info_alunos["alunos"]
    aluno.append(r)
    return jsonify(r)

@app.route('/professores', methods=['POST'])
def createProfessores():
    r = request.json
    aluno = info_professores["professores"]
    aluno.append(r)
    return jsonify(r)

@app.route('/turmas', methods=['POST'])
def createTurma():
    r = request.json
    aluno = info_turmas["turmas"]
    aluno.append(r)
    return jsonify(r)
#-----------------------------------POST------------------------------------
#-----------------------------------PUT------------------------------------
@app.route('/alunos/<int:idAluno>', methods=['PUT'])
def updateAluno(idAluno):
    alunos = info_alunos["alunos"]
    for aluno in alunos:
        if aluno['id'] == idAluno:
          r = request.json
          if 'nome' in r:
            aluno['nome'] =r['nome']
          if 'idade' in r:
            aluno['idade'] =r['idade']
          if 'data_nascimento' in r:
            aluno['data_nascimento'] =r['data_nascimento']
          if 'nota_primeiro_semestre' in r:
            aluno['nota_primeiro_semestre'] =r['nota_primeiro_semestre']
          if 'nota_segundo_semestre' in r:
            aluno['nota_segundo_semestre'] =r['nota_segundo_semestre']
          
          return jsonify(r)
        
@app.route('/professores/<int:idProfessor>', methods=['PUT'])
def updateProfessor(idProfessor):
    professores = info_professores["professores"]
    for professor in professores:
        if professor['id'] == idProfessor:
          r = request.json
          if 'nome' in r:
            professor['nome'] =r['nome']
          if 'idade' in r:
            professor['idade'] =r['idade']
          if 'materia' in r:
            professor['materia'] =r['materia']
          if 'observacoes' in r:
            professor['observacoes'] =r['observacoes']
          return jsonify(r), 200
    
    return jsonify({"error":"Aluno não encontrado"}),200
     

@app.route('/turmas/<int:idTurma>', methods=['PUT'])
def updateTurma(idTurma):
    turmas = info_turmas["turmas"]
    for turma in turmas:
        if turma['id'] == idTurma:
          r = request.json
          turma['descricao'] =r['descricao']
          turma['ativo'] =r['ativo']
          return jsonify(r)
          
#-----------------------------------PUT------------------------------------


#-----------------------------------GET------------------------------------
@app.route('/alunos', methods=['GET'])
def getAlunos():
    dados = info_alunos["alunos"]
    return jsonify(dados)

@app.route('/professores', methods=['GET'])
def getProfessores():
    dados = info_professores["professores"]
    return jsonify(dados)

@app.route('/turmas', methods=['GET'])
def getTurmas():
    dados = info_turmas["turmas"]
    return jsonify(dados)
#-----------------------------------GET------------------------------------

#-----------------------------------DELETE------------------------------------

@app.route('/alunos/<int:idAluno>', methods=['DELETE'])
def deleteAluno(idAluno):
    alunos = info_alunos["alunos"]   
    for aluno in alunos:
        if aluno['id'] == idAluno:
            alunos.remove(aluno)
            return jsonify({"REMOVIDO": aluno})

@app.route('/professores/<int:idProfessor>', methods=['DELETE'])
def deleteProfessor(idProfessor):
    professores = info_professores["professores"]   
    for professor in professores:
        if professor['id'] == idProfessor:
            professores.remove(professor)
            return jsonify({"REMOVIDO": professor})

@app.route('/turmas/<int:idTurma>', methods=['DELETE'])
def deleteTurma(idTurma):
    turmas = info_turmas["turmas"]   
    for turma in turmas:
        if turma['id'] == idTurma:
            turmas.remove(turma)
            return jsonify({"REMOVIDO": turma})

#-----------------------------------DELETE------------------------------------


if __name__ == '__main__':
    app.run(debug=True)
