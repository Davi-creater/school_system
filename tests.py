import requests
import unittest

class Testes(unittest.TestCase):
    def teste_url_alunos(self):
        r = requests.get('http://localhost:5000/alunos')
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina ")

    def teste_url_professores(self):
        r = requests.get('http://localhost:5000/professores')
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina ")

    def teste_url_turmas(self):
        r = requests.get('http://localhost:5000/turmas')
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina ")

    def teste_adiciona_alunos(self):
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

    def teste_adiciona_professores(self):
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
            self.fail('aluno fernando nao apareceu na lista de professores')
        if not achei_odair:
            self.fail('aluno roberto nao apareceu na lista de professores')
    
    def teste_adiciona_turmas(self):
        r = requests.post('http://localhost:5000/turmas',json={'descricao':'portugues','id':1, "professor_id": 1})
        r = requests.post('http://localhost:5000/turmas',json={'descricao':'matematica','id':2, "professor_id": 1})
        r_lista = requests.get('http://localhost:5000/turmas')
        lista_retornada = r_lista.json()
        achei_portugues = False
        achei_matematica = False
        for aluno in lista_retornada:
            if aluno['descricao'] == 'portugues':
                achei_portugues = True
            if aluno['descricao'] == 'matematica':
                achei_matematica = True
        if not achei_portugues:
            self.fail('aluno fernando nao apareceu na lista de alunos')
        if not achei_matematica:
            self.fail('aluno roberto nao apareceu na lista de alunos')

        
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testes)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()