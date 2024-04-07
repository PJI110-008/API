from flask import Flask, Blueprint
from connect_mysql import conectar
import json
import mysql.connector

# Cria um objeto Blueprint para as rotas
bp_rotas = Blueprint('rotas', __name__)

# Define as rotas dentro do blueprint
@bp_rotas.route('/')
def index():
    try:
        conexao = conectar()
        
        if conexao is None:
            return []
        cursor = conexao.cursor()

        sql = "SELECT * from 9756_idade_cor_ou_raça"
        cursor.execute(sql)
        resultado = cursor.fetchall()

        # Obter os nomes das colunas
        colunas = [desc[0] for desc in cursor.description]

        # Construir os dicionários para cada linha do resultado
        resultado_dict = []
        for row in resultado:
            row_dict = {}
            for i, value in enumerate(row):
                row_dict[colunas[i]] = value
            resultado_dict.append(row_dict)

    except mysql.connector.Error as erro:
        print(f"Erro ao conecar com o banco de dados: {erro}")
        resultado_dict = []
    finally:
        cursor.close()
        conexao.close()
        return json.dumps(resultado_dict)
   

