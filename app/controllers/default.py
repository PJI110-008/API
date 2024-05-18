from app import app, db
from app.models.tables import IdadeCorOuRaca, RendimentoPcd
from app.funcs.req_main import consultaAPI
from flask import jsonify
import pandas as pd

@app.route('/health-check')
def health_check():
    return "API OK"

@app.route('/', methods=['GET'])
def index():
    results = IdadeCorOuRaca.query.all()
    print(results)
    results_dict = [result.to_dict() for result in results]
    return jsonify(results_dict)

@app.route('/populate', methods=['GET'])
def populate():
    #Caso o arquivo rendimento_pdc mude de local, ajustar o caminho abaixo
    file_path = 'docs/rendimento_pdc.xlsx'
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

    if not RendimentoPcd.query.first(): 
        df = pd.read_excel(file_path, skiprows=3, usecols="A:D")
            # Renomeia as colunas
        df.columns = ["Rotulos de Linha", "Pessoa com Deficiência", "Pessoa sem Deficiência", "Total Geral"]
            # Processa os dados para adicionar sufixos
        processed_rows = []
        current_gender = None
        for index, row in df.iterrows():
            if pd.isna(row["Rotulos de Linha"]):
                    continue
            elif row["Rotulos de Linha"] in ["Homens", "Mulheres", "Total"]:
                    current_gender = row["Rotulos de Linha"]
            else:
                if current_gender == "Homens":
                    prefix = "h_"
                elif current_gender == "Mulheres":
                    prefix = "m_"
                elif current_gender == "Total":
                    prefix = ""
                else:
                    prefix = ""
                processed_rows.append({
                    "rotulo": prefix + row["Rotulos de Linha"].strip(),
                    "pessoa_com_deficiencia": row["Pessoa com Deficiência"],
                    "pessoa_sem_deficiencia": row["Pessoa sem Deficiência"]
                    #,"total_geral": row["Total Geral"]
                })
            #return processed_rows
        for row in processed_rows:
            rotulo = row['rotulo']
            pessoa_com_deficienciaprint = row['pessoa_com_deficiencia']
            pessoa_sem_deficiencia = row['pessoa_sem_deficiencia']
            i = RendimentoPcd(rotulo,pessoa_com_deficienciaprint,pessoa_sem_deficiencia)
            db.session.add(i)
            db.session.commit()
        return 'DATA INSERTED'
    else:
        return 'DATA ALREADY IN USE'
