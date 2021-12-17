from flask import Flask
from flask_bootstrap import Bootstrap
from portfolio.db import db
from portfolio.models.user import User
from portfolio.models.project import Project
from portfolio.models.language import Language

app = Flask(__name__,instance_relative_config=True)
Bootstrap(app)

app.config.from_pyfile('setup.py', silent=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

db.init_app(app)

with app.app_context():
    db.create_all()


from portfolio.routes import views



