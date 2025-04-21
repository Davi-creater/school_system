import requests
import unittest

class Testes(unittest.TestCase):
    def teste_url_alunos_001(self):
        r = requests.get('http://localhost:5000/alunos')
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina ")

    def teste_url_professores_002(self):
        r = requests.get('http://localhost:5000/professores')
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina ")

    def teste_url_turmas_003(self):
        r = requests.get('http://localhost:5000/turmas')
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina ")

    def teste_adiciona_alunos_004(self):
        r = requests.post('http://localhost:5000/alunos',json={'nome':'fernando','id':1, 'turma_id':1})
        r = requests.post('http://localhost:5000/alunos',json={'nome':'roberto','id':2,'turma_id':1})
        r_lista = requests.get('http://localhost:5000/alunos')
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

    def teste_adiciona_professores_005(self):
        r = requests.post('http://localhost:5000/professores',json={'nome':'caio','id':1})
        r = requests.post('http://localhost:5000/professores',json={'nome':'odair','id':2})
        r_lista = requests.get('http://localhost:5000/professores')
        lista_retornada = r_lista.json()
        achei_caio = False
        achei_odair = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'caio':
                achei_caio = True
            if aluno['nome'] == 'odair':
                achei_odair = True
        if not achei_caio:
            self.fail('professor caio nao apareceu na lista de professores')
        if not achei_odair:
            self.fail('professor odair nao apareceu na lista de professores')
    
    def teste_adiciona_turmas_006(self):
     r = requests.post('http://localhost:5000/turmas', json={'descricao': 'portugues', 'id': 1, "professor_id": 1})
     r = requests.post('http://localhost:5000/turmas', json={'descricao': 'matematica', 'id': 2, "professor_id": 1})
     
     
     r_lista = requests.get('http://localhost:5000/turmas')
     lista_retornada = r_lista.json()
     
     achei_portugues = False
     achei_matematica = False
     
     
     for turma in lista_retornada:
         if turma['descricao'] == 'portugues':
             achei_portugues = True
         if turma['descricao'] == 'matematica':
             achei_matematica = True
     
     
     if not achei_portugues:
         self.fail('turma portugues nao apareceu na lista de turmas')
     if not achei_matematica:
         self.fail('turma matematica nao apareceu na lista de turmas')


    def teste_deleta_aluno_007(self):
        r_post = requests.post('http://localhost:5000/alunos', json={'nome': 'AlunoDeletar', 'id': 999, 'turma_id': 1})
        self.assertEqual(r_post.status_code, 201)
        r_delete = requests.delete('http://localhost:5000/alunos/999')
        self.assertEqual(r_delete.status_code, 200)
        r_get = requests.get('http://localhost:5000/alunos/999')
        self.assertEqual(r_get.status_code, 404)

    def teste_deleta_professor_008(self):
        r_post = requests.post('http://localhost:5000/professores', json={'nome': 'ProfessorDeletar', 'id': 999})
        self.assertEqual(r_post.status_code, 201)
        r_delete = requests.delete('http://localhost:5000/professores/999')
        self.assertEqual(r_delete.status_code, 200)
        r_get = requests.get('http://localhost:5000/professores/999')
        self.assertEqual(r_get.status_code, 404)

    def teste_deleta_turma_009(self):
        r_post = requests.post('http://localhost:5000/turmas', json={'descricao': 'TurmaDeletar', 'id': 999, "professor_id": 1})
        self.assertEqual(r_post.status_code, 201)
        r_delete = requests.delete('http://localhost:5000/turmas/999')
        self.assertEqual(r_delete.status_code, 200)
        r_get = requests.get('http://localhost:5000/turmas/999')
        self.assertEqual(r_get.status_code, 404)


    def teste_busca_aluno_por_id_010(self):
        r_post = requests.post('http://localhost:5000/alunos', json={'nome': 'AlunoBusca', 'id': 888, 'turma_id': 1})
        self.assertEqual(r_post.status_code, 201)

        r_get = requests.get('http://localhost:5000/alunos/888')
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()['nome'], 'AlunoBusca')

        r_get_inexistente = requests.get('http://localhost:5000/alunos/9999')
        self.assertEqual(r_get_inexistente.status_code, 404)

    def teste_busca_professor_por_id_011(self):
        r_post = requests.post('http://localhost:5000/professores', json={'nome': 'ProfessorBusca', 'id': 888})
        self.assertEqual(r_post.status_code, 201)

        r_get = requests.get('http://localhost:5000/professores/888')
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()['nome'], 'ProfessorBusca')

        r_get_inexistente = requests.get('http://localhost:5000/professores/9999')
        self.assertEqual(r_get_inexistente.status_code, 404)

    def teste_busca_turma_por_id_012(self):
        r_post = requests.post('http://localhost:5000/turmas', json={'descricao': 'TurmaBusca', 'id': 888, "professor_id": 1})
        self.assertEqual(r_post.status_code, 201)

        r_get = requests.get('http://localhost:5000/turmas/888')
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()['descricao'], 'TurmaBusca')

        r_get_inexistente = requests.get('http://localhost:5000/turmas/9999')
        self.assertEqual(r_get_inexistente.status_code, 404)

    def teste_atualiza_aluno_011(self):
        r_post = requests.post('http://localhost:5000/alunos', json={'nome': 'AlunoAtualizar', 'id': 777, 'turma_id': 1})
        self.assertEqual(r_post.status_code, 201)

        r_put = requests.put('http://localhost:5000/alunos/777', json={'nome': 'AlunoAtualizado'})
        self.assertEqual(r_put.status_code, 200)

        r_get = requests.get('http://localhost:5000/alunos/777')
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()['nome'], 'AlunoAtualizado')

    def teste_atualiza_professor_012(self):
        r_post = requests.post('http://localhost:5000/professores', json={'nome': 'ProfessorAtualizar', 'id': 777})
        self.assertEqual(r_post.status_code, 201)

        r_put = requests.put('http://localhost:5000/professores/777', json={'nome': 'ProfessorAtualizado'})
        self.assertEqual(r_put.status_code, 200)

        r_get = requests.get('http://localhost:5000/professores/777')
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()['nome'], 'ProfessorAtualizado')

    def teste_atualiza_turma(self): 
    
        r_post = requests.post('http://localhost:5000/turmas', json={
            'id': 777,
            'nome': 'Turma Teste',
            'turno': 'Matutino',
            'professor_id': 1,
            'ativo': True,
            'descricao': 'Turma para teste'
    })
        self.assertEqual(r_post.status_code, 201)  

    
        r_put = requests.put('http://localhost:5000/turmas/777', json={
            'nome': 'Turma Atualizada',
            'turno': 'Vespertino',
            'professor_id': 1,
            'ativo': True,
            'descricao': 'TurmaAtualizada'
    })
        self.assertEqual(r_put.status_code, 200)

        r_get = requests.get('http://localhost:5000/turmas/777')
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()['descricao'], 'TurmaAtualizada')


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testes)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()