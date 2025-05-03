from config import db

class Turmas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    turno = db.Column(db.String(30))
    professor = db.relationship("Professor", back_populates="turmas")
    professor_id = db.Column(db.Integer, db.ForeignKey("professor.id"), nullable=False)
    alunos = db.relationship("Aluno", back_populates="turma")


    def __init__(self, nome, turno, professor_id):

        self.nome = nome
        self.turno = turno
        self.professor_id = professor_id

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'turno': self.turno, 'professor_id': self.professor_id}

# info_turmas = {
#     "turmas": [
#         {
#             "id": 1,
#             "nome": "Turma A",
#             "turno": "Matutino",
#             "professor_id": 1,
#             "ativo": True,
#             "descricao": "portugues"
#         }
#     ]
# }

def createTurmas(r):

    
    # if any(turma['id'] == r['id'] for turma in getTurmas["turmas"]):
    #      return {"erro": "ID da turma já existe"}
    nova_turma = Turmas(
        nome=r['nome'],
        turno=r['turno'],
        professor_id=int(r['professor_id']),
    )
    db.session.add(nova_turma)
    db.session.commit()
    return{"mensagem":r}
    # info_turmas["turmas"].append(r)
    # return {"mensagem": "Turma criada com sucesso", "turma": r}

def getTurmas():
    turmas = Turmas.query.all()
    return[turma.to_dict() for turma in turmas]
    # return info_turmas["turmas"]

def getTurmaId(idTurma):
    turma = Turmas.query.get(idTurma)
    if not turma:
        return{"error": "Turma não encontrado"}
    return turma.to_dict()
    # for turma in info_turmas["turmas"]: 
    #     if turma["id"] == idTurma:
    #         return turma
    # return None

def updateTurma(idTurma, novos_dados):
    turma = Turmas.query.get(idTurma)
    if not turma:
        return{"error": "Turma não encontrado"}
    campos_validos = [
        'nome',
        'turno',
        'professor_id',
        'ativo',
        'descricao'
    ]

    for campo in campos_validos:
        if campo in novos_dados:
            setattr(turma, campo, novos_dados[campo])

    db.session.commit()
    # turma = getTurmaId(idTurma)
    # if not turma:
    #     return {"erro": "Turma não encontrada"}

    
    # turma.update({key: value for key, value in novos_dados.items() if key != "id"})

    # return {"mensagem": "Turma atualizada", "turma": turma}

def deleteTurma(idTurma):
    turma = Turmas.query.get(idTurma)
    if not turma:
        return{"error": "Turma não encontrado"}
    db.session.delete(turma)
    db.session.commit()

    # turma = getTurmaId(idTurma)
    # if turma:
    #     info_turmas["turmas"].remove(turma) 
    #     return {"mensagem": "Turma removida"}
    # return {"erro": "Turma não encontrada"}
