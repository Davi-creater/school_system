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
    # Validação de ID único antes de adicionar uma nova turma
    if any(turma['id'] == r['id'] for turma in info_turmas["turmas"]):
        return {"erro": "ID da turma já existe"}
    info_turmas["turmas"].append(r)
    return {"mensagem": "Turma criada com sucesso", "turma": r}

def getTurmas():
    return info_turmas["turmas"]

def getTurmaId(idTurma):
    for turma in info_turmas["turmas"]:  # Corrigido para "turmas"
        if turma["id"] == idTurma:
            return turma
    return None

def updateTurma(idTurma, novos_dados):
    turma = getTurmaId(idTurma)
    if not turma:
        return {"erro": "Turma não encontrada"}
    dados = ['nome', 'professor_id', 'turno', 'ativo']
    # Verifica se todos os campos necessários estão no novo dados e não estão vazios
    #if not all(campo in novos_dados and novos_dados[campo] not in [None, ""] for campo in dados):
    #    return {"erro": "Preencher todos os campos"}
    # Atualiza a turma com os novos dados
    turma.update({key: value for key, value in novos_dados.items() if key != "id"})
    return {"mensagem": "Turma atualizada", "turma": turma}

def deleteTurma(idTurma):
    turma = getTurmaId(idTurma)
    if turma:
        info_turmas["turmas"].remove(turma)  # Corrigido para acessar "turmas"
        return {"mensagem": "Turma removida"}
    return {"erro": "Turma não encontrada"}