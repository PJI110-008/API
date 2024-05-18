from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/Database_PI'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import tables
from app.controllers import default
