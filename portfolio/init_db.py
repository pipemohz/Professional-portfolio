from db import db
from models import User,Project, Language

db.create_all()
admin = User(username='admin', email='pipemoreno9405@gmail.com')
db.session.add(admin)

db.session.commit()