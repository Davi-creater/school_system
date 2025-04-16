
from turmas.model_turmas import getTurmas
info_alunos = {
    "alunos": []
}

def createAlunos(r):
    
    turma_existe = any(turma['id'] == r['turma_id'] for turma in getTurmas()) 
    if not turma_existe:
        return {"erro": "Turma não existe"}

    
    if "nome" not in r or not r["nome"].strip():
        return {"erro": "Nome não pode estar vazio"}

    
    info_alunos["alunos"].append(r)
    return {"mensagem": "Aluno criado com sucesso", "aluno": r}

def getAlunos():
    return info_alunos["alunos"]

def getAlunoId(idAluno):
    for aluno in info_alunos["alunos"]:
        if aluno["id"] == idAluno:
            return aluno
    return None

def updateAluno(idAluno, novos_dados):
    aluno = getAlunoId(idAluno)
    if not aluno:
        return {"erro": "Aluno não encontrado"}

    aluno.update({key: value for key, value in novos_dados.items() if key != "id"})
    return {"mensagem": "Aluno atualizado", "aluno": aluno}

def deleteAluno(idAluno):
    aluno = getAlunoId(idAluno)
    if aluno:
        info_alunos["alunos"].remove(aluno)
        return {"mensagem": "Aluno removido"}
    return {"erro": "Aluno não encontrado"}
