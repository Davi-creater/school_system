from flask_restx import Namespace, Resource, fields 
from professores.model_professores import createProfessor, getProfessores, getProfessorId, updateProfessor, deleteProfessor

professor_ns = Namespace("Professores", description="Área relacionada aos professores")

professor_model = professor_ns.model("Professores", {
    "name" : fields.String(required=True, description="Nome do professor(a)"),
    "idade" : fields.Integer(required=True, description="Idade do professor(a),"),
    "data_nascimento" : fields.Float(required=True, description="Data de nascimento"),

})

professor_output_model = professor_ns.model("Professores_Saída", {
    "name" : fields.String( description="Nome do professor(a)"),
    "idade" : fields.Integer( description="Idade do professor(a),"),
    "data_nascimento" : fields.Float( description="Data de nascimento"),
    "id_professor" : fields.Integer(description="ID do professor"),
    "disciplina" : fields.String(description="Disciplina do professor"),
    "salário" : fields.Float(description="Salário do Professor(a)"),
    "turmas" : fields.Integer(description="Turmas relacionadas ao professor"),


})

@professor_ns.route("/")
class ProfessoresResource(Resource):
    @professor_ns.marshal_list_with(professor_output_model)
    def get(self):
        "Lista todos os professores"
        return getProfessores
    

    @professor_ns.expect(professor_model)
    def post(self):
        "Cria um novo professor"
        data = professor_ns.payload
        response, status_code = createProfessor(data)
        return response, status_code

@professor_ns.route("/<int:id_professor>")
class ProfessorIdResource(Resource):
    @professor_ns.marshal_with(professor_output_model)
    def get(self, id_professor):
        """Obtém um professor pelo ID"""
        return getProfessorId(id_professor)
    
    @professor_ns.expect(professor_model)
    def put(self, id_professor):
        """Atualiza professor pelo ID"""
        data = professor_ns.payload
        updateProfessor(id_professor, data)
        return data, 200
    
    def delete(self, id_professor):
        """Exclui professor pelo ID"""
        deleteProfessor(id_professor)
        return {"message": "Professor excluído com sucesso"}, 200