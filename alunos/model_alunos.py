from config import db
from turmas.model_turmas import getTurmas
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.String(10))
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)
    turma = db.relationship("Turmas", back_populates="alunos")
    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=False)

    def __init__(self, nome, idade, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final, turma_id):
       
        self.nome = nome
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = media_final
        self.turma_id = turma_id

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'idade': self.idade, 'data_nascimento': self.data_nascimento, 'nota_primeiro_semestre': self.nota_primeiro_semestre, 'nota_segundo_semestre': self.nota_segundo_semestre, 'media_final': self.media_final, 'turma_id': self.turma_id}

info_alunos = {
    "alunos": []
}


def createAlunos(r):
    
    turma_existe = any(turma['id'] == r['turma_id'] for turma in getTurmas()) 
    if not turma_existe:
        return {"erro": "Turma não existe"}

    
    if "nome" not in r or not r["nome"].strip():
        return {"erro": "Nome não pode estar vazio"}

    novo_aluno = Aluno(
     nome=r['nome'],
     idade=r['idade'],
     data_nascimento=r['data_nascimento'],
     nota_primeiro_semestre=float(r['nota_primeiro_semestre']),
     nota_segundo_semestre=float(r['nota_segundo_semestre']),
     turma_id=int(r['turma_id']),
     media_final=(
            float(r['nota_primeiro_semestre']) + float(r['nota_segundo_semestre'])
        ) / 2,
    )
    
    db.session.add(novo_aluno)
    db.session.commit()
    #info_alunos["alunos"].append(r)
    return {"mensagem": "Aluno criado com sucesso", "aluno": r}

def getAlunos():
    alunos =   Aluno.query.all()
    return[aluno.to_dict() for aluno in alunos]
    #return info_alunos["alunos"]

def getAlunoId(idAluno):
    aluno = Aluno.query.get(idAluno)
    if not aluno:
        return{"error": "Aluno não encontrado"}
    return aluno.to_dict()
    # for aluno in info_alunos["alunos"]:
    #     if aluno["id"] == idAluno:
    #         return aluno
    # return None

def updateAluno(idAluno, novos_dados):
    aluno = Aluno.query.get(idAluno)
    if not aluno:
        return{"error": "Aluno não encontrado"}
    campos_validos = [
        'nome',
        'idade',
        'data_nascimento',
        'nota_primeiro_semestre',
        'nota_segundo_semestre',
        'media_final',
        'turma_id'
    ]

    for campo in campos_validos:
        if campo in novos_dados:
            setattr(aluno, campo, novos_dados[campo])

    db.session.commit()
    
    # aluno = getAlunoId(idAluno)
    # if not aluno:
    #     return {"erro": "Aluno não encontrado"}

    # aluno.update({key: value for key, value in novos_dados.items() if key != "id"})
    # return {"mensagem": "Aluno atualizado", "aluno": aluno}

def deleteAluno(idAluno):
    aluno = Aluno.query.get(idAluno)
    if not aluno:
        return{"error": "Aluno não encontrado"}
    db.session.delete(aluno)
    db.session.commit()
    # aluno = getAlunoId(idAluno)
    # if aluno:
    #     info_alunos["alunos"].remove(aluno)
    #     return {"mensagem": "Aluno removido"}
    # return {"erro": "Aluno não encontrado"}
