from db.db import MYSQLConnection

class Utils:

    def verifica_cobertura(id_endereco, id_parceiro):

        try:
            with MYSQLConnection() as (con, cur):
                cur.execute('SELECT uf FROM tb_viabilidades WHERE id = {};'.format(id_endereco))
                uf_endereco = cur.fetchone()

                cur.execute('SELECT uf_cobertura FROM tb_parceiros WHERE id = {};'.format(id_parceiro))
                uf_parceiro = cur.fetchone()
            
            if uf_endereco is None:
                return 'Endereço não encontrado.'
            if uf_parceiro is None:
                return 'Parceiro não encontrado.'        

            if uf_endereco['uf'].upper() in uf_parceiro['uf_cobertura'].upper():
                return True
            return 'Este parceiro não atende a este endereço.'
        except Exception as e:
            print(f'Erro ao verificar cobertura: {e}')
            return 'Erro no processamento da requisição.'
    
    def parceiro_repondeu(id_endereco, id_parceiro):

        try:
            with MYSQLConnection() as (con, cur):
                cur.execute('''SELECT id FROM tb_resultados_viabilidades
                    WHERE id_viabilidade = {} AND id_parceiro = {};'''.format(id_endereco, id_parceiro))
                data = cur.fetchone()
            
            if data is None:
                return False
            return 'Este parceiro já respondeu este endereço.'
        except Exception as e:
            print(f'Erro ao verificar se o parceiro respondeu: {e}')
            return 'Erro no processamento da requisição.'
    
    def retorno_existe(id_retorno):

        try:
            with MYSQLConnection() as (con, cur):
                cur.execute('''SELECT id FROM tb_resultados_viabilidades
                    WHERE id = {};'''.format(id_retorno))
                data = cur.fetchone()
            
            if data is None:
                return 'Este retorno não existe.'
            return True
        except Exception as e:
            print(f'Erro ao verificar se existe retorno: {e}')
            return 'Erro no processamento da requisição.'



print(Utils.verifica_cobertura(1, 3))