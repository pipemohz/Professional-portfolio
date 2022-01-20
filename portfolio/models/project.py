from portfolio.db import db
from sqlalchemy.orm import relationship
from portfolio.models.language import Language
from portfolio.models.project_language import association_table


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(2000), nullable=False)
    languages = relationship("Language", secondary=association_table)
