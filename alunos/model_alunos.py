info_alunos = {
    "alunos": [
        {
            "id": 1,
            "nome": "Davi",
            "idade": "19",
            "turma_id": 1,
            "data_nascimento": "21/09/2005",
            "nota_primeiro_semestre": "10",
            "nota_segundo_sementre": "10",
            "media_final": "10"
        }
    ]
}

def createAlunos(r ,turmas ):
    #dados = ['nome', 'turma_id', 'data_nascimento', 'nota_primeiro_semestre','nota_segundo_semestre']
    #if not all(dado in r for dado in dados):
        #return{"error":"campos obrigatorios"}
    
    turmas_verificacao = any(turma['id']== r['turma_id'] for turma in turmas) 
    if not turmas_verificacao:
        return{"erro": "Turma nao existe"}
    info_alunos["alunos"].append(r)

def getAlunos():
    return info_alunos["alunos"]

def getAlunoId(idAluno):
    for aluno in info_alunos["alunos"]:
        if aluno["id"] == idAluno:
            return aluno
    return None

def updateAluno(idAluno,novos_dados):
    aluno = getAlunoId(idAluno)
    if not aluno:
        return{"erro":"aluno nao encontrado"}
    dados = ['nome', 'turma_id', 'data_nascimento', 'nota_primeiro_semestre','nota_segundo_semestre']
    if not all(campo in novos_dados and novos_dados[campo]not in [none,""]for campo in dados):
        return{"erro":"preencher todos os campos"}
    aluno.update({key: value for key, value in novos_dados.items()if key != "id"})
    return{"mensagem":"aluno atualizado", "aluno":aluno}

def deleteAluno(idAluno):
    aluno = getAlunoId(idAluno)
    if aluno:
        info_alunos.remove(aluno)
        return{"mensagem":"aluno removido"}
    return{"erro": "aluno nao encontrado"}
