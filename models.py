from cotacao import db

class Viabilidade(db.Model):
    __tablename__ = 'viabilidade'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.String(20))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    uf = db.Column(db.String(2))
    produto = db.Column(db.String(45))
    velocidade = db.Column(db.String(45))

    def __repr__(self) -> str:
        return f'<Name {self.name}>'
print(Viabilidade)

class Parceiro(db.Model):
    __tablename__ = 'parceiro'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    uf_cobertura = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f'<Name {self.name}>'

class ResultadoViabilidade(db.Model):
    __tablename__ = 'resultado_viabilidade'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resultado = db.Column(db.String(45), nullable=False)
    id_viabilidade = db.Column(db.Integer, db.ForeignKey('viabilidade'))
    id_parceiro = db.Column(db.Integer, db.ForeignKey('parceiro'))
    viabilidade = db.relationship('Viabilidade', back_populates='resultado_viabilidade')
    parceiro = db.relationship('Parceiro', back_populates='resultado_viabilidade')

'''
class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f'<Name {self.name}>'
'''