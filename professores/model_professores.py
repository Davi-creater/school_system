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
    info_professores["professores"].append(r)
    return {"mensagem": "Professor criado com sucesso", "professor": r}

def getProfessores():
    return info_professores["professores"]

def getProfessorId(idProfessor):
    for professor in info_professores["professores"]:
        if professor["id"] == idProfessor:
            return professor
    return None

def updateProfessor(idProfessor, novos_dados):
    professor = getProfessorId(idProfessor)
    if not professor:
        return {"erro": "professor não encontrado"}

    dados = ['nome', 'data_nascimento', 'disciplina', 'salario']
    #if not all(campo in novos_dados and novos_dados[campo] not in [None, ""] for campo in dados):
    #    return {"erro": "preencher todos os campos"}

    professor.update({key: value for key, value in novos_dados.items() if key != "id"})
    return {"mensagem": "professor atualizado", "professor": professor}

def deleteProfessor(idProfessor):
    professor = getProfessorId(idProfessor)
    if professor:
        info_professores["professores"].remove(professor) 
        return {"mensagem": "professor removido"}
    return {"erro": "professor nao encontrado"}
