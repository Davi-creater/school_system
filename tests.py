import requests
import unittest

class Testes(unittest.TestCase):
    def teste_url_alunos(self):
        r = requests.get('http://localhost:8000/alunos')
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina ")

    def teste_url_professores(self):
        r = requests.get('http://localhost:8000/professores')
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina ")

    def teste_url_turmas(self):
        r = requests.get('http://localhost:8000/turmas')
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina ")

    def teste_adiciona_alunos(self):
        r = requests.post('http://localhost:8000/alunos',json={'nome':'fernando','id':1, 'turma_id':1})
        r = requests.post('http://localhost:8000/alunos',json={'nome':'roberto','id':2,'turma_id':1})
        r_lista = requests.get('http://localhost:8000/alunos')
        lista_retornada = r_lista.json()
        achei_fernando = False
        achei_roberto = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'fernando':
                achei_fernando = True
            if aluno['nome'] == 'roberto':
                achei_roberto = True
        if not achei_fernando:
            self.fail('aluno fernando nao apareceu na lista de alunos')
        if not achei_roberto:
            self.fail('aluno roberto nao apareceu na lista de alunos')

    def teste_adiciona_professores(self):
        r = requests.post('http://localhost:8000/professores',json={'nome':'caio','id':1})
        r = requests.post('http://localhost:8000/professores',json={'nome':'odair','id':2})
        r_lista = requests.get('http://localhost:8000/professores')
        lista_retornada = r_lista.json()
        achei_caio = False
        achei_odair = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'caio':
                achei_caio = True
            if aluno['nome'] == 'odair':
                achei_odair = True
        if not achei_caio:
            self.fail('aluno fernando nao apareceu na lista de professores')
        if not achei_odair:
            self.fail('aluno roberto nao apareceu na lista de professores')
    
    def teste_adiciona_turmas(self):
     r = requests.post('http://localhost:8000/turmas', json={'descricao': 'portugues', 'id': 1, "professor_id": 1})
     r = requests.post('http://localhost:8000/turmas', json={'descricao': 'matematica', 'id': 2, "professor_id": 1})
     
     # Obtendo a lista de turmas
     r_lista = requests.get('http://localhost:8000/turmas')
     lista_retornada = r_lista.json()
     
     achei_portugues = False
     achei_matematica = False
     
     # Verificando se as turmas estão na lista retornada
     for turma in lista_retornada:
         if turma['descricao'] == 'portugues':
             achei_portugues = True
         if turma['descricao'] == 'matematica':
             achei_matematica = True
     
     # Mensagens de erro corrigidas
     if not achei_portugues:
         self.fail('turma portugues nao apareceu na lista de turmas')
     if not achei_matematica:
         self.fail('turma matematica nao apareceu na lista de turmas')


    def teste_deleta_aluno(self):
        r_post = requests.post('http://localhost:8000/alunos', json={'nome': 'AlunoDeletar', 'id': 999, 'turma_id': 1})
        self.assertEqual(r_post.status_code, 201)
        r_delete = requests.delete('http://localhost:8000/alunos/999')
        self.assertEqual(r_delete.status_code, 200)
        r_get = requests.get('http://localhost:8000/alunos/999')
        self.assertEqual(r_get.status_code, 404)

    def teste_deleta_professor(self):
        r_post = requests.post('http://localhost:8000/professores', json={'nome': 'ProfessorDeletar', 'id': 999})
        self.assertEqual(r_post.status_code, 201)
        r_delete = requests.delete('http://localhost:8000/professores/999')
        self.assertEqual(r_delete.status_code, 200)
        r_get = requests.get('http://localhost:8000/professores/999')
        self.assertEqual(r_get.status_code, 404)

    def teste_deleta_turma(self):
        r_post = requests.post('http://localhost:8000/turmas', json={'descricao': 'TurmaDeletar', 'id': 999, "professor_id": 1})
        self.assertEqual(r_post.status_code, 201)
        r_delete = requests.delete('http://localhost:8000/turmas/999')
        self.assertEqual(r_delete.status_code, 200)
        r_get = requests.get('http://localhost:8000/turmas/999')
        self.assertEqual(r_get.status_code, 404)


    def teste_busca_aluno_por_id(self):
        r_post = requests.post('http://localhost:8000/alunos', json={'nome': 'AlunoBusca', 'id': 888, 'turma_id': 1})
        self.assertEqual(r_post.status_code, 201)

        r_get = requests.get('http://localhost:8000/alunos/888')
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()['nome'], 'AlunoBusca')

        r_get_inexistente = requests.get('http://localhost:8000/alunos/9999')
        self.assertEqual(r_get_inexistente.status_code, 404)

    def teste_busca_professor_por_id(self):
        r_post = requests.post('http://localhost:8000/professores', json={'nome': 'ProfessorBusca', 'id': 888})
        self.assertEqual(r_post.status_code, 201)

        r_get = requests.get('http://localhost:8000/professores/888')
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()['nome'], 'ProfessorBusca')

        r_get_inexistente = requests.get('http://localhost:8000/professores/9999')
        self.assertEqual(r_get_inexistente.status_code, 404)

    def teste_busca_turma_por_id(self):
        r_post = requests.post('http://localhost:8000/turmas', json={'descricao': 'TurmaBusca', 'id': 888, "professor_id": 1})
        self.assertEqual(r_post.status_code, 201)

        r_get = requests.get('http://localhost:8000/turmas/888')
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()['descricao'], 'TurmaBusca')

        r_get_inexistente = requests.get('http://localhost:8000/turmas/9999')
        self.assertEqual(r_get_inexistente.status_code, 404)

    def teste_atualiza_aluno(self):
        r_post = requests.post('http://localhost:8000/alunos', json={'nome': 'AlunoAtualizar', 'id': 777, 'turma_id': 1})
        self.assertEqual(r_post.status_code, 200)

        r_put = requests.put('http://localhost:8000/alunos/777', json={'nome': 'AlunoAtualizado'})
        self.assertEqual(r_put.status_code, 200)

        r_get = requests.get('http://localhost:8000/alunos/777')
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()['nome'], 'AlunoAtualizado')

    def teste_atualiza_professor(self):
        r_post = requests.post('http://localhost:8000/professores', json={'nome': 'ProfessorAtualizar', 'id': 777})
        self.assertEqual(r_post.status_code, 201)

        r_put = requests.put('http://localhost:8000/professores/777', json={'nome': 'ProfessorAtualizado'})
        self.assertEqual(r_put.status_code, 200)

        r_get = requests.get('http://localhost:8000/professores/777')
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()['nome'], 'ProfessorAtualizado')

    def teste_atualiza_turma(self):
    # Criar a turma completa
     r_post = requests.post('http://localhost:8000/turmas', json={
         'id': 777,
         'nome': 'Turma Teste',
         'turno': 'Matutino',
         'professor_id': 1,
         'ativo': True,
         'descricao': 'Turma para teste'
     })
     self.assertEqual(r_post.status_code, 200)  # 201 porque a rota retorna (json, 201)
 
     # Atualizar todos os campos
     r_put = requests.put('http://localhost:8000/turmas/777', json={
         'nome': 'Turma Atualizada',
         'turno': 'Vespertino',
         'professor_id': 1,
         'ativo': True,
         'descricao': 'TurmaAtualizada'
     })
     self.assertEqual(r_put.status_code, 200)
 
     r_get = requests.get('http://localhost:8000/turmas/777')
     self.assertEqual(r_get.status_code, 200)
     self.assertEqual(r_get.json()['descricao'], 'TurmaAtualizada')


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testes)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()