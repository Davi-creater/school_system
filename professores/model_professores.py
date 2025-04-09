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

def createProfessor(r):
    #dados = ['nome', 'data_nascimento', 'disiplina','salario']
    #if not all(dado in r for dado in dados):
     #   return{"error":"campos obrigatorios"}
    info_professores["professores"].append(r)

def getProfessores():
    return info_professores["professores"]

def getProfessorId(idProfessor):
    for professor in info_professores["professores"]:
        if professor["id"] == idProfessor:
            return professor
    return None

def updateProfessor(idProfessor,novos_dados):
    professor = getProfessorId(idProfessor)
    if not professor:
        return{"erro":"aluno nao encontrado"}
    dados = ['nome', 'data_nascimento', 'disiplina','salario']
    if not all(campo in novos_dados and novos_dados[campo]not in [none,""]for campo in dados):
        return{"erro":"preencher todos os campos"}
    professor.update({key: value for key, value in novos_dados.items()if key != "id"})
    return{"mensagem":"aluno atualizado", "professor":professor}

def deleteProfessor(idProfessor):
    professor = getProfessorId(idProfessor)
    if professor:
        info_professores.remove(professor)
        return{"mensagem":"professor removido"}
    return{"erro": "professor nao encontrado"}
