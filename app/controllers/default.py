from app import app, db
from app.models.tables import IdadeCorOuRaca
from app.funcs.req_main import consultaAPI

@app.route('/health-check')
def health_check():
    return "API OK"

@app.route('/', methods=['GET'])
def index():
    r = IdadeCorOuRaca.query.all()
    print(r)
    return 'OK'

@app.route('/populate', methods=['GET'])
def populate():
    if not IdadeCorOuRaca.query.first(): 
        data = consultaAPI('https://servicodados.ibge.gov.br/api/v3/agregados/9756/periodos/2022/variaveis/10613|8845?localidades=N2[all]&classificacao=86[2777,2778,2779,2780]')
        
        for resultado in data[0]['resultados']:
        # Iterar sobre as categorias
            for categoria_id, categoria_valor in resultado['classificacoes'][0]['categoria'].items():
            # Verificar se o identificador da categoria está presente
                if categoria_id in resultado['classificacoes'][0]['categoria']:
                    cor_raca = resultado['classificacoes'][0]['categoria'][categoria_id]
                    for serie in resultado['series']:
                        grande_regiao = serie['localidade']['nome']
                        for ano, valor in serie['serie'].items():
                            i = IdadeCorOuRaca(cor_raca, grande_regiao, ano, valor)
                            db.session.add(i)
                            db.session.commit()
        return 'DATA INSERTED'
    else:
        return 'DATA ALREADY IN USE'
