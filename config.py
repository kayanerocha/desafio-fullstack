from decouple import config

SECRET_KEY = config('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD = config('MYSQL_SGBD'),
        user = config('MYSQL_USER'),
        password = config('MYSQL_PASSWORD'),
        server = config('MYSQL_SERVER'),
        database = config('MYSQL_DATABASE')
    )

# # Pega o caminho absoluto do diretório que esse arquivo (__file__) está e acessa o uploads
# UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '\\uploads'