from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)

from app import models
from app import routes
