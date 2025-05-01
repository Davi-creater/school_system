import os
from config import app,db
from alunos.controller_alunos import alunos_blueprint
from professores.controller_professores import professores_blueprint
from turmas.controller_turmas import turmas_blueprint
from sqlalchemy import inspect

app.register_blueprint(alunos_blueprint)
app.register_blueprint(professores_blueprint)
app.register_blueprint(turmas_blueprint)

with app.app_context():
    db.create_all()
    print("Tabelas criadas")
    inspector = inspect(db.engine)
    print(inspector.get_table_names())

if __name__ == '__main__':
    app.run(host=app.config["HOST"],port = app.config['PORT'],debug=app.config['DEBUG'])
