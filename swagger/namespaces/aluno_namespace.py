from flask_restx import Namespace, Resource, fields 
from alunos.model_alunos import createAlunos, getAlunos, getAlunoId, updateAluno, deleteAluno

alunos_ns = Namespace("alunos", description="Área relacionada aos alunos")

aluno_model = alunos_ns.model("Aluno",{
    "nome" : fields.String(required=True, description="Nome do Aluno(a)"),
    "data_nascimento" : fields.String(required=True, description="Data de nascimento (AAAA-MM-DD)"),
    "nota_1_semestre" : fields.Float(required=True, description="Nota do primeiro semestre"),
    "nota_2_semestre" : fields.Float(required=True, description="Nota do segundo semestre"),
    "turma_id" : fields.Integer(required=True, description="ID da turma associada"),

})

aluno_output_model = alunos_ns.model("Alunos_Saída", {
    "id" : fields.Integer(description="ID do aluno(a)"),
    "nome" : fields.String(description="Nome do aluno(a)"),
    "idade" : fields.Integer(description="Idade do aluno(a)"),
    "data_nascimento" : fields.String(description="Data de nascimento (AAAA-MM-DD)"),
    "nota_1_semestre" : fields.Float(description="Nota do primeiro semestre"),
    "nota_2_semestre" : fields.Float(description="Nota do segundo semestre"),
    "media_final" : fields.Float(description="Media final do aluno(a)"),
    "turma_id" : fields.Integer(description="ID da turma associeda"),
})

@alunos_ns.route("/")
class AlunosResource(Resource):
    @alunos_ns.marshal_list_with(aluno_output_model)
    def get(self):
        """Lista todos os alunos"""
        return getAlunos()

    @alunos_ns.expect(aluno_model)
    def post(self):
        """Cria um novo aluno"""
        data = alunos_ns.payload
        response, status_code = createAlunos(data)
        return response, status_code

@alunos_ns.route("/<int:id_aluno>")
class AlunoIdResource(Resource):
    @alunos_ns.marshal_with(aluno_output_model)
    def get(self, id_aluno):
        """Obtém um aluno pelo ID"""
        return getAlunoId(id_aluno)

    @alunos_ns.expect(aluno_model)
    def put(self, id_aluno):
        """Atualiza um aluno pelo ID"""
        data = alunos_ns.payload
        updateAluno(id_aluno, data)
        return data, 200

    def delete(self, id_aluno):
        """Exclui um aluno pelo ID"""
        deleteAluno(id_aluno)
        return {"message": "Aluno excluído com sucesso"}, 200