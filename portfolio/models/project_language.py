from sqlalchemy.sql.schema import ForeignKey
from portfolio.db import db


association_table = db.Table('association', db.Model.metadata,
    db.Column('project_id', db.Integer(), db.ForeignKey('projects.id')),
    db.Column('language_id', db.Integer(), db.ForeignKey('languages.id'))
)