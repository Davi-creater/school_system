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

def createTurmas(r ,professores):
   # dados = ['nome', 'professor_id', 'turno', 'ativo']
    #if not all(dado in r for dado in dados):
      #  return{"error":"campos obrigatorios"}
    
    #professor_verificacao = any(professor['id']== r['turma_id'] for professor in professores) 
    #if not professor_verificacao:
        #return{"erro": "Professor nao existe"}
    info_turmas["turmas"].append(r)

def getTurmas():
    return info_turmas["turmas"]

def getTurmaId(idTurma):
    for turma in info_turmas["turma"]:
        if turma["id"] == idTurma:
            return turma
    return None

def updateTurma(idTurma,novos_dados):
    turma = getTurmaId(idTurma)
    if not turma:
        return{"erro":"turma nao encontrado"}
    dados = ['nome', 'professor_id', 'turno', 'ativo']
    if not all(campo in novos_dados and novos_dados[campo]not in [none,""]for campo in dados):
        return{"erro":"preencher todos os campos"}
    turma.update({key: value for key, value in novos_dados.items()if key != "id"})
    return{"mensagem":"turma atualizado", "turma":turma}

def deleteTurma(idTurma):
    turma = getTurmaId(idTurma)
    if turma:
        info_turmas.remove(turma)
        return{"mensagem":"turma removido"}
    return{"erro": "turma nao encontrado"}