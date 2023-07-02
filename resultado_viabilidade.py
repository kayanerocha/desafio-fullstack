from cotacao import app
from db.db import MYSQLConnection
from flask import request, Response
from utils import Utils
import json

@app.route('/')
def index():
    try:
        with MYSQLConnection() as (con, cur):
            query = '''SELECT a.id, concat(b.logradouro, ', ', b.numero, ' - ', b.bairro, ', ', b.cidade, ' - ', b.uf) AS endereco,
                a.resultado, c.nome AS nome_parceiro
                FROM tb_resultados_viabilidades a
                LEFT JOIN tb_viabilidades b ON b.id = a.id_viabilidade
                LEFT JOIN tb_parceiros c ON c.id = a.id_parceiro;'''
            cur.execute(query)
            data = cur.fetchall()

        return Response(response=json.dumps({'data': data, 'status': 200, 'message': ''}),
            status=200,
            content_type='application/json',
            headers={'Access-Control-Allow-Origin': '*'})
    except Exception as e:
        print(f'Erro ao buscar os resultado de viabilidades: {e}')
        return Response(response=json.dumps({'data': None, 'status': 500,
            'message': 'Erro no processamento da requisição.'}),
            status=500,
            content_type='application/json',
            headers={'Access-Control-Allow-Origin': '*'})

@app.route('/enviar-resultado/<id_viabilidade>/<id_parceiro>', methods=['POST'])
def criar(id_viabilidade, id_parceiro):
    try:
        data = request.get_json()
        resultado = data['resultado']

        parceiro_atende = Utils.verifica_cobertura(id_viabilidade, id_parceiro)
        retorno_existe = Utils.parceiro_repondeu(id_viabilidade, id_parceiro)

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
    
@app.route('/atualizar/<id_retorno>', methods=['PUT'])
def atualizar(id_retorno):
    try:
        data = request.get_json()
        resultado = data['resultado']

        retorno_existe = Utils.retorno_existe(id_retorno)

        if retorno_existe is True:
            with MYSQLConnection() as (con, cur):
                query = '''UPDATE tb_resultados_viabilidades
                SET resultado = '{}'
                WHERE id = {};'''.format(resultado, id_retorno)
                cur.execute(query)
                con.commit()

            return Response(response=json.dumps({'data': None, 'status': 200, 'message': 'Resultado atualizado com sucesso.'}),
                status=200,
                content_type='application/json')
        else:
            return Response(response=json.dumps({'data': None, 'status': 200, 'message': retorno_existe}),
                status=200,
                content_type='application/json')
    except Exception as e:
        print(f'Erro ao salvar resultado: {e}')
        return Response(response=json.dumps({'data': None, 'status': 500, 'message': 'Erro no processamento da requisição.'}),
            status=500,
            content_type='application/json')

@app.route('/deletar/<id_retorno>', methods=['DELETE'])
def deletar(id_retorno):
    try:
        retorno_existe = Utils.retorno_existe(id_retorno)

        if retorno_existe is True:
            with MYSQLConnection() as (con, cur):
                query = 'DELETE FROM tb_resultados_viabilidades WHERE id = {};'.format(id_retorno)
                cur.execute(query)
                con.commit()

            return Response(response=json.dumps({'data': None, 'status': 200, 'message': 'Resultado deletado com sucesso.'}),
                status=200,
                content_type='application/json')
        else:
            return Response(response=json.dumps({'data': None, 'status': 200, 'message': retorno_existe}),
                status=200,
                content_type='application/json')
    except Exception as e:
        print(f'Erro ao salvar resultado: {e}')
        return Response(response=json.dumps({'data': None, 'status': 500, 'message': 'Erro no processamento da requisição.'}),
            status=500,
            content_type='application/json')
    
