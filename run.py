import os
import sys
from portfolios import create_app
from portfolios.db import db
from flask_script import Manager
from flask_migrate import Migrate
from flask.cli import cli


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

cli.main(args=sys.argv[1:])

if __name__ == '__main__':
    manager.run()