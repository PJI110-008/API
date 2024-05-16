# coding=utf-8
import mysql.connector

def conectar():
    try:
        # Estabelecendo a Conexao com o banco de dados
        conexao = mysql.connector.connect(
            host="host.docker.internal",
            user="root",
            password="root",
            database="Database_PI"
        )
        
        # Verificando se a Conexao foi bem sucedida
        if conexao.is_connected():
            print("Conexao bem-sucedida!")
            return conexao
    except mysql.connector.Error as erro:
        print("Erro ao conecar com o banco de dados: %s" % erro)
        return None
