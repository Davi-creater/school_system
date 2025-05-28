# SCHOOL - SYSTEM

## 📄 Descrição da API

Este projeto utiliza a funcionalidade de Blueprints do Flask para organizar e modularizar o código da aplicação web. Blueprints permitem separar diferentes partes da aplicação em componentes reutilizáveis e de fácil manutenção, como rotas, templates e arquivos estáticos.
API básica para a gestão de Professores, Turmas e Alunos utilizando o framework Flask. A API permite operações de CRUD (Create, Read, Update, Delete) e retornar respostas em formato JSON, sendo testada com ferramentas como o Postman. 
A colaboração no projeto foi gerenciada por meio de um repositório no GitHub

### Principais Endpoints
- Classe professores
- `GET http://localhost:5000/professores` — Retorna dados específicos 
- `POST http://localhost:5000/professores` — Cria um novo registro
- `PUT http://localhost:5000/professores/id` — Atualiza informações existentes
- `DELETE http://localhost:5000/professores/id` — Remove um registro

- Classe alunos
- `GET http://localhost:5000/alunos` — Retorna dados específicos 
- `POST http://localhost:5000/alunos` — Cria um novo registro
- `PUT http://localhost:5000/alunos/id` — Atualiza informações existentes
- `DELETE http://localhost:5000/alunos/id` — Remove um registro
- Classe turmas
- `GET http://localhost:5000/turmas` — Retorna dados específicos 
- `POST http://localhost:5000/turmas` — Cria um novo registro
- `PUT http://localhost:5000/turmas/id` — Atualiza informações existentes
- `DELETE http://localhost:5000/turmas/id` — Remove um registro

---

## 🚀 Instruções de Execução (com Docker)

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Executando o serviço

1. Clone o repositório:
   ```bash
   git clone https://github.com/Davi-creater/school_system.git
   cd school_system

2. Abrir o docker de sugundo plano 
3. No terminal dar os seguntes comandos para que a api esteja rodando:
   docker-compose build
   docker-compose up
4. Parar a execuçao da api de o seguinte comando:
   docker-compose down

