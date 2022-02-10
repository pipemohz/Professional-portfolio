from portfolios.db import db
from sqlalchemy.orm import relationship
from portfolios.models.language import Language
from portfolios.models.project_language import association_table


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(2000), nullable=False)
    languages = relationship("Language", secondary=association_table)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'))
    portfolio = relationship("Portfolio", back_populates="projects")
