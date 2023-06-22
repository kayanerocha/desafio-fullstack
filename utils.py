from db.db import MYSQLConnection

class Utils:

    def verifica_cobertura(id_endereco, id_parceiro):
        with MYSQLConnection() as (con, cur):
            cur.execute('SELECT uf FROM tb_viabilidades WHERE id = {};'.format(id_endereco))
            id_endereco = cur.fetchone()

            cur.execute('SELECT uf_cobertura FROM tb_viabilidades WHERE id = {};'.format(id_endereco))

        
        if id_endereco is None:
            return 'Endereço não encontrado.'
        

        print(id_endereco)
        # if uf_endereco.upper() == uf_parceiro.upper():
        #     return True
        # return False

Utils.verifica_cobertura(4, 1)