from portfolios.db import db
from sqlalchemy.orm import relationship


class Portfolio(db.Model):
    __tablename__ = "portfolios"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    date_created = db.Column(db.Date, nullable=False)
    date_modified = db.Column(db.Date, nullable=False)
    projects = relationship("Project", back_populates='portfolio', cascade="all, delete")
    manager = relationship("User", back_populates="portfolios")
    manager_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
