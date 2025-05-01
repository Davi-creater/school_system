from config import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.String(10))
    disciplina = db.Column(db.String(100))
    salario = db.Column(db.Integer)

    def __init__(self, id, nome, idade, data_nascimento, disciplina, salario):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.disciplina = disciplina
        self.salario = salario

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'idade': self.idade, 'data_nascimento': self.data_nascimento, 'disciplina': self.disciplina, 'salario': self.salario}

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
