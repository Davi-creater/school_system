info_turmas = {
    "turmas": [
        {
            "id": 1,
            "nome": "Turma A",
            "turno": "Matutino",
            "professor_id": 1,
            "ativo": True,
            "descricao": "portugues"
        }
    ]
}

def createTurmas(r):
    
    if any(turma['id'] == r['id'] for turma in info_turmas["turmas"]):
        return {"erro": "ID da turma já existe"}
    info_turmas["turmas"].append(r)
    return {"mensagem": "Turma criada com sucesso", "turma": r}

def getTurmas():
    return info_turmas["turmas"]

def getTurmaId(idTurma):
    for turma in info_turmas["turmas"]: 
        if turma["id"] == idTurma:
            return turma
    return None

def updateTurma(idTurma, novos_dados):
    turma = getTurmaId(idTurma)
    if not turma:
        return {"erro": "Turma não encontrada"}

    
    turma.update({key: value for key, value in novos_dados.items() if key != "id"})

    return {"mensagem": "Turma atualizada", "turma": turma}

def deleteTurma(idTurma):
    turma = getTurmaId(idTurma)
    if turma:
        info_turmas["turmas"].remove(turma) 
        return {"mensagem": "Turma removida"}
    return {"erro": "Turma não encontrada"}
