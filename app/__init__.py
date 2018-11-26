from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

app = Flask(__name__, static_folder="static", template_folder="templates", static_url_path='/static')
app.config.from_object(Config)
heroku = Heroku(app)
db = SQLAlchemy(app)


def get_db():
    return db


from app import model
from app import routes
