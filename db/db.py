from decouple import config
import mysql.connector

class MYSQLConnection(object):

    def _connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=config('MYSQL_HOST'),
                user=config('MYSQL_USER'),
                password=config('MYSQL_PASSWORD'),
                database=config('MYSQL_DATABASE'),
                port=config('MYSQL_PORT'),
                connect_timeout=5
            )
            self.cur = self.conn.cursor()

        except Exception as e:
            print(f'Erro ao se conectar no banco de dados: {e}')
            raise e

    def __enter__(self, *args, **kwargs):
        self._connect()
        return (self.conn, self.cur)

    def __exit__(self, *args):
        if self.conn is not None:
            self.conn.close()