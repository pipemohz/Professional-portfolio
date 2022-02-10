from flask import Blueprint

main = Blueprint('main', __name__)

from portfolios.routes import views