import mysql.connector

def conectar():
    try:
        # Estabelecendo a conexão com o banco de dados
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )
        
        # Verificando se a conexão foi bem sucedida
        if conexao.is_connected():
            print("Conexão bem-sucedida!")
            return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None