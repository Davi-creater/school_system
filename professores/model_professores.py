from config import db

class Professor(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.String(10))
    disciplina = db.Column(db.String(100))
    salario = db.Column(db.Integer)
    turmas = db.relationship("Turmas", back_populates="professor")
    

    def __init__(self,nome, idade, data_nascimento, disciplina, salario):
        
        self.nome = nome
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.disciplina = disciplina
        self.salario = salario

    def to_dict(self):
        return {
            'id': self.id, 
            'nome': self.nome, 
            'idade': self.idade, 
            'data_nascimento': self.data_nascimento, 
            'disciplina': self.disciplina, 
            'salario': self.salario
        }

# Função para criar um novo professor
def createProfessor(r):
    novo_professor = Professor(
        
        nome=r['nome'],
        idade=int(r['idade']),
        data_nascimento=r['data_nascimento'],
        disciplina=r['disciplina'],
        salario=int(r['salario']),
    )
    db.session.add(novo_professor)
    db.session.commit()
    return {"mensagem": "Professor criado com sucesso", "professor": novo_professor.to_dict()}

# Função para obter todos os professores
def getProfessores():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

# Função para obter um professor pelo ID
def getProfessorId(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        return {"error": "Professor não encontrado"}
    return professor.to_dict()

# Função para atualizar os dados de um professor
def updateProfessor(idProfessor, novos_dados):
    professor = Professor.query.get(idProfessor)
    if not professor:
        return {"error": "Professor não encontrado"}
    
    campos_validos = ['nome', 'data_nascimento', 'salario', 'disciplina']

    for campo in campos_validos:
        if campo in novos_dados:
            setattr(professor, campo, novos_dados[campo])

    db.session.commit()
    return {"mensagem": "Professor atualizado com sucesso", "professor": professor.to_dict()}

# Função para excluir um professor
def deleteProfessor(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        return {"error": "Professor não encontrado"}
    
    db.session.delete(professor)
    db.session.commit()
    return {"mensagem": "Professor removido com sucesso"}
