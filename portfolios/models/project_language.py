from sqlalchemy.sql.schema import ForeignKey, Table
from portfolios.db import db


association_table = db.Table('languages_project', db.Model.metadata,
                             db.Column('project_id', db.Integer(),
                                       db.ForeignKey('projects.id')),
                             db.Column('language_id', db.Integer(),
                                       db.ForeignKey('languages.id'))
                             )
