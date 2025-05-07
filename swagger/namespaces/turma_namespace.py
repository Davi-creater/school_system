from flask_restx import Namespace, Resource, fields 
from turmas.model_turmas import createTurmas,getTurmas,getTurmaId,updateTurma, deleteTurma


turmas_ns = Namespace("turmas", description="Área relacionada às turmas")

turma_model = turmas_ns.model("Turma", {
    "nome" : fields.String(required=True, description="Nome da Turma"),
    "turno" : fields.String(required=True, description="Turno da turma"),
    "professor" : fields.String(required=True, description="Professor da Turma"),
    "professor_id" : fields.Integer(required=True, description="Id do professor da turma")

     }
)

turma_output_model = turmas_ns.model("Turma_saída", {
    "id" : fields.Integer(description="ID da Turma"),
    "nome" : fields.String(description="Nome da Turma"),
    "turno" : fields.String(description="Turno da turma"),
    "professor" : fields.String(description="Professor da Turma"),
    "professor_id" : fields.Integer(description="Id do professor da turma"),
    "alunos" : fields.String(description="Alunos da turma")

}
)


@turmas_ns.route("/")
class TurmasResource(Resource):
    @turmas_ns.marshal_list_with(turma_output_model)
    def get(self):
        "Lista todas as turmas"
        return getTurmas
    
    @turmas_ns.expect(turma_model)
    def post(self):
        "Cria uma nova turma"
        data = turmas_ns.payload
        response, status_code = createTurmas(data)
        return response, status_code
    

@turmas_ns.route("/<int:id_turma>")
class TurmaIdResource(Resource):
    @turmas_ns.marshal_with(turma_output_model)
    def get(self, id_turma):
        """Obtém turma pelo ID"""
        return getTurmaId(id_turma)

    @turmas_ns.expect(turma_model)
    def put(self, id_turma):
        """Atualiza turma pelo ID"""
        data = turmas_ns.payload
        updateTurma(id_turma, data)
        return data, 200
    
    def delete(self, id_turma):
        """Exclui turma pelo ID"""
        deleteTurma(id_turma)
        return {"message": "Turma excluído com sucesso"}, 200
    


