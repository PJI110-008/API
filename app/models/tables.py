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
    
    def to_dict(self):
        return {
            'id': self.id,
            'cor_ou_raca': self.cor_ou_raca,
            'grande_regiao': self.grande_regiao,
            'ano': self.ano,
            'porcentagem': self.porcentagem,
        }
########################################################################

class RendimentoPcd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rotulo = db.Column(db.String(100), index=True, nullable=False)
    pessoa_com_deficiencia = db.Column(db.Integer, nullable=False)
    pessoa_sem_deficiencia = db.Column(db.Integer, nullable=False)

    def __init__(self, rotulo, pessoa_com_deficiencia, pessoa_sem_deficiencia):
        self.rotulo = rotulo
        self.pessoa_com_deficiencia = pessoa_com_deficiencia
        self.pessoa_sem_deficiencia = pessoa_sem_deficiencia
    
    def __repr__(self):
        return '<RendimentoPcd %r>' % self.rotulo
    
    def to_dict(self):
        return {
            'id': self.id,
            'pessoa_com_deficiencia': self.pessoa_com_deficiencia,
            'pessoa_sem_deficiencia': self.pessoa_sem_deficiencia,
            'rotulo': self.rotulo
        }
