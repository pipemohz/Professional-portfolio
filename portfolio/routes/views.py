from crypt import methods
from flask import abort, flash
from flask_login import login_required, LoginManager, login_user, logout_user
from werkzeug.utils import redirect
from portfolio import app
from flask.helpers import url_for
from flask.templating import render_template
from portfolio.forms.forms import ProjectForm, LoginForm, RegisterForm
from portfolio.dao import *
from portfolio.models.user import User

login = LoginManager()
login.init_app(app)


@login.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@login.unauthorized_handler
def unauthorized():
    return abort(401, 'You must be logged in to access this route')


@app.route('/index')
@app.route('/', methods=['GET', 'POST'])
def index():
    projects = get_projects()
    return render_template('index.html', projects=projects)


@app.route('/contact')
def contact():
    return render_template('contact.html')

# FIXME: Error in delete button for languages field after validation of form


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user(form)
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if get_user(form):
            user = get_user(form)
            if valid_password(user, form.password.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash(message="The password does not match.")
        else:
            flash(message="The user does not exists.")
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ProjectForm()
    if form.validate_on_submit():
        if form.languages.entries:
            create_project(form=form)
        return redirect(url_for('index'))
    return render_template('add.html', form=form, action='add')


@app.route('/delete/<int:id>', methods=['GET'])
@login_required
def delete(id):
    delete_project(project_id=id)
    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    form = ProjectForm()
    if form.validate_on_submit():
        update_project(project_id=id, form=form)
        return redirect(url_for('index'))
    return render_template('add.html', form=form, action=f'edit', project_id=id)
