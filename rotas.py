from flask import Flask, Blueprint
from connect_mysql import conectar
import json
import mysql.connector

# Cria um objeto Blueprint para as rotas
bp_rotas = Blueprint('rotas', __name__)

@bp_rotas.route('/consulta/<ano>')
def consulta_por_ano(ano):
    try:
        conexao = conectar()
        
        if conexao is None:
            return []
        cursor = conexao.cursor()

        sql = f"SELECT * from tabela WHERE Ano = {ano}"
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

        cursor.close()
        conexao.close()
        return json.dumps(resultado_dict)
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar com o banco de dados: {erro}")
        resultado_dict = []
        return json.dumps(resultado_dict)
