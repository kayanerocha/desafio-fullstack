from cotacao import app
from db.db import MYSQLConnection
from flask import request

app.route('/')
def index():
    with MYSQLConnection() as (con, cur):
        query = ''''''

app.route('/enviar-resultado/<id_viabilidade>/<id_parceiro>', methods=['POST'])
def criar(id_viabilidade, id_parceiro):
    data = request.get_json()
    resultado = data['resultado']

    with MYSQLConnection() as (con, cur):
        query = '''INSERT INTO tb_resultados_viabilidades (resultado, id_viabilidade, id_parceiro)
            values (%s, %d, %d)'''.format(resultado, id_viabilidade, id_parceiro)
        cur.execute(query)
        con.commit()

