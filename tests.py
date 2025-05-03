import requests
import unittest

class Testes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Limpa registros
        for tipo in ['alunos', 'professores', 'turmas']:
            r = requests.get(f'http://localhost:5000/{tipo}')
            if r.status_code == 200:
                for item in r.json():
                    requests.delete(f'http://localhost:5000/{tipo}/{item["id"]}')

        # Cria professor (ID 1)
        requests.post('http://localhost:5000/professores', json={
            'id': 1, 'nome': 'Professor Único', 'idade': 40,
            "data_nascimento": "1985-01-01", "disciplina": "Matemática", "salario": 5000
        })

        # Cria turma (ID 1)
        requests.post('http://localhost:5000/turmas', json={
            'id': 1, 'nome': 'Turma Única', 'turno': "Manhã",
            "professor_id": 1, "descricao": "Turma de teste", "ativo": True
        })

        # Cria aluno (ID 1)
        requests.post('http://localhost:5000/alunos', json={
            'id': 1, 'nome': 'Aluno Único', 'idade': 15,
            'data_nascimento': '2010-01-01', 'turma_id': 1,
            'nota_primeiro_semestre': 7.5, 'nota_segundo_semestre': 8.0
        })

    def teste_001(self):
        r = requests.get('http://localhost:5000/alunos')
        self.assertNotEqual(r.status_code, 404, "Página /alunos não definida")

    def teste_002(self):
        r = requests.get('http://localhost:5000/professores')
        self.assertNotEqual(r.status_code, 404, "Página /professores não definida")

    def teste_003(self):
        r = requests.get('http://localhost:5000/turmas')
        self.assertNotEqual(r.status_code, 404, "Página /turmas não definida")

    def teste_004_lista_professor(self):
        r = requests.get('http://localhost:5000/professores')
        self.assertTrue(any(p['nome'] == 'Professor Único' for p in r.json()), 'Professor Único não apareceu na lista')

    def teste_005_lista_turma(self):
        r = requests.get('http://localhost:5000/turmas')
        self.assertTrue(any(t['nome'] == 'Turma Única' for t in r.json()), 'Turma Única não apareceu na lista')

    def teste_006_lista_aluno(self):
        r = requests.get('http://localhost:5000/alunos')
        self.assertTrue(any(a['nome'] == 'Aluno Único' for a in r.json()), 'Aluno Único não apareceu na lista')

    def teste_007_busca_aluno_por_id(self):
        r = requests.get('http://localhost:5000/alunos/1')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['nome'], 'Aluno Único')

    def teste_008_busca_professor_por_id(self):
        r = requests.get('http://localhost:5000/professores/1')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['nome'], 'Professor Único')

    def teste_009_busca_turma_por_id(self):
        r = requests.get('http://localhost:5000/turmas/1')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['nome'], 'Turma Única')

    def teste_010_atualiza_aluno(self):
        r = requests.put('http://localhost:5000/alunos/1', json={'nome': 'Aluno Atualizado'})
        self.assertEqual(r.status_code, 200)
        r = requests.get('http://localhost:5000/alunos/1')
        self.assertEqual(r.json()['nome'], 'Aluno Atualizado')

    def teste_011_atualiza_professor(self):
        r = requests.put('http://localhost:5000/professores/1', json={'nome': 'Professor Atualizado'})
        self.assertEqual(r.status_code, 200)
        r = requests.get('http://localhost:5000/professores/1')
        self.assertEqual(r.json()['nome'], 'Professor Atualizado')

    def teste_012_atualiza_turma(self):
        r = requests.put('http://localhost:5000/turmas/1', json={'nome': 'Nova descrição'})
        self.assertEqual(r.status_code, 200)
        r = requests.get('http://localhost:5000/turmas/1')
        self.assertEqual(r.json()['nome'], 'Nova descrição')

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testes)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == '__main__':
    runTests()
