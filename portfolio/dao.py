from portfolio import db
from portfolio.models.project import Project

def get_projects():
    return db.session.query(Project).all()

