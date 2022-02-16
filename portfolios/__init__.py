from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from portfolios.db import db
from config import config
from flask_ckeditor import CKEditor


bootstrap = Bootstrap()
login = LoginManager()
ckeditor = CKEditor()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login.init_app(app)
    ckeditor.init_app(app)

    from portfolios.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

