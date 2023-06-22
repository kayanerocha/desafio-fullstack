from cotacao import app
from db.db import MYSQLConnection
from flask import request, Response
from utils import Utils
import json

@app.route('/')
def index():
    with MYSQLConnection() as (con, cur):
        query = ''''''

@app.route('/enviar-resultado/<id_viabilidade>/<id_parceiro>', methods=['POST'])
def criar(id_viabilidade, id_parceiro):
    try:
        data = request.get_json()
        resultado = data['resultado']

        parceiro_atende = Utils.verifica_cobertura(id_viabilidade, id_parceiro)
        retorno_existe = Utils.retorno_existe(id_viabilidade, id_parceiro)

        message = ''
        if parceiro_atende is not True:
            message = f'{parceiro_atende} '
        if retorno_existe is not False:
            message += retorno_existe

        if parceiro_atende is True and retorno_existe is False:
            with MYSQLConnection() as (con, cur):
                query = '''INSERT INTO tb_resultados_viabilidades (resultado, id_viabilidade, id_parceiro)
                    values ('{}', {}, {})'''.format(resultado, id_viabilidade, id_parceiro)
                cur.execute(query)
                con.commit()

            return Response(response=json.dumps({'data': None, 'status': 200, 'message': 'Resultado salvo com sucesso.'}),
                status=200,
                content_type='application/json')
        else:
            return Response(response=json.dumps({'data': None, 'status': 200, 'message': message}),
                status=200,
                content_type='application/json')
    except Exception as e:
        print(f'Erro ao salvar resultado: {e}')
        return Response(response=json.dumps({'data': None, 'status': 500, 'message': 'Erro no processamento da requisição.'}),
                status=500,
                content_type='application/json')

