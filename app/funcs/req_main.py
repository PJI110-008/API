import requests
def consultaAPI(url: str) -> dict:
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
