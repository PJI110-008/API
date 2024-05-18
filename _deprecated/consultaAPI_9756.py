# coding=utf-8
import requests
from connect_mysql import conectar

def consultaAPI_9756_idade_cor_ou_raca(url: str) -> dict:
    try:
        
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            # Retorna os dados JSON da resposta
            return resposta.json()
        else:
            # Se a resposta não foi bem-sucedida, imprime a mensagem de erro
            print(f"Erro ao fazer requisição: {resposta.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Se ocorrer um erro durante a requisição, imprime a exceção
        print(f"Erro durante a requisição: {e}")
        return None

# Função para inserir os dados no banco de dados
def insert_data_into_database(conn, cor_raca, grande_regiao, porcentagem):
    cur = conn.cursor()
    query = f"INSERT INTO 9756_idade_cor_ou_raca (Cor_ou_raca, Grande_Regiao, Ano, Porcentagem) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (cor_raca, grande_regiao, ano, porcentagem))
    conn.commit()
    cur.close()



# Conectar ao banco de dados
conn = conectar()
url= 'https://servicodados.ibge.gov.br/api/v3/agregados/9756/periodos/2022/variaveis/10613|8845?localidades=N2[all]&classificacao=86[2777,2778,2779,2780]'
data = consultaAPI_9756_idade_cor_ou_raca(url)

# Iterar sobre os resultados
for resultado in data[0]['resultados']:
    # Iterar sobre as categorias
    for categoria_id, categoria_valor in resultado['classificacoes'][0]['categoria'].items():
        # Verificar se o identificador da categoria está presente
        if categoria_id in resultado['classificacoes'][0]['categoria']:
            cor_raca = resultado['classificacoes'][0]['categoria'][categoria_id]
            for serie in resultado['series']:
                grande_regiao = serie['localidade']['nome']
                for ano, valor in serie['serie'].items():
                    # Inserir os dados no banco de dados
                    insert_data_into_database(conn, cor_raca, grande_regiao, ano, valor)

# Fechar a conexão com o banco de dados
conn.close()

