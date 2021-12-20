from werkzeug.utils import redirect
from portfolio import app
from flask import request
from flask.helpers import url_for
from flask.templating import render_template
from portfolio.forms.forms import ProjectForm
from portfolio.dao import *



@app.route('/index')
@app.route('/', methods=['GET'])
def index():
    projects = get_projects()
    return render_template('index.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

#FIXME: Error in delete button for languages field after validation of form

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ProjectForm()
    if form.validate_on_submit():
        for entry in form.languages.entries:
            print(entry.data)
        return redirect(url_for('index'))
    return render_template('add.html', form=form)
