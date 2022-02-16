activate_this = '/var/www/delco/portfolioapp/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys, os
sys.path.insert(0, '/var/www/delco/portfolioapp/')    

from portfolios import create_app
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


application = create_app(os.environ.get('FLASK_CONFIG') or 'default')



