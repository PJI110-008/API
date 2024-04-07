#!/usr/bin/python

from flask import Flask, jsonify
from rotas import bp_rotas

app = Flask(__name__)

# Registrar as rotas do blueprint
app.register_blueprint(bp_rotas)

app.run(host='0.0.0.0')


