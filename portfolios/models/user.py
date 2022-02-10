from portfolios.db import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    portfolios = relationship("Portfolio", back_populates='manager')
