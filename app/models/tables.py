from app import db

class IdadeCorOuRaca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cor_ou_raca = db.Column(db.String(100), index=True, nullable=False)
    grande_regiao = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.String(100), nullable=False)
    porcentagem = db.Column(db.Integer)

    def __init__(self, cor_ou_raca, grande_regiao, ano, porcentagem):
        self.cor_ou_raca = cor_ou_raca
        self.grande_regiao = grande_regiao
        self.ano = ano
        self.porcentagem = porcentagem
    
    def __repr__(self):
        return '<IdadeCorOuRaca %r>' % self.cor_ou_raca