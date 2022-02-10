from datetime import datetime
from portfolios.main import main
from flask import abort, flash, request, session
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.utils import redirect
from flask.helpers import url_for
from flask.templating import render_template
from portfolios.forms.forms import PortfolioForm, ProjectForm, LoginForm, RegisterForm, MailForm
from portfolios.dao import *
from portfolios.models.user import User
from portfolios import login
from portfolios.email import send_email


@login.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@login.unauthorized_handler
def unauthorized():
    return abort(401, 'You must be logged in to access this route')


@main.route('/index')
@main.route('/', methods=['GET', 'POST'])
def index():
    portfolios = get_portfolios()
    return render_template('index.html', portfolios=portfolios)


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = MailForm()
    if form.validate_on_submit():
        send_email(form=form)
        return redirect(url_for('.index'))
    return render_template('contact.html', form=form)

# FIXME: Error in delete button for languages field after validation of form
# COMPLETED: Create routes for portfolios creation and private management of portfolios
# view of all portfolios registered in plattform (like journals) and single view of
# portfolio's projects.
# COMPLETED: Define access roles for secure accesss of users to its own portfolios


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user(form)
        return redirect(url_for('.index'))
    return render_template('register.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash(message="You are already logged in.")
        return redirect(url_for('.index'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            if get_user(form):
                user = get_user(form)
                if valid_password(user, form.password.data):
                    login_user(user)
                    return redirect(url_for('.manager'))
                else:
                    flash(message="The password does not match.")
            else:
                flash(message="The user does not exists.")
        return render_template('login.html', form=form)


@main.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))


@main.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PortfolioForm()
    if form.validate_on_submit():
        create_portfolio(form=form, user=current_user)
        return redirect(url_for('.manager'))
    return render_template('createPortfolio.html', form=form)


@main.route('/portfolios/view/<int:portfolio_id>', methods=['GET'])
def portfolio_view(portfolio_id):
    portfolio = get_portfolio_by_id(portfolio_id)
    if current_user.is_authenticated:
        user_id = int(current_user.get_id())
    else:
        user_id = None
    session['portfolio_id'] = portfolio.id
    return render_template('portfolio.html', portfolio=portfolio, user_id=user_id)


@main.route('/portfolios/delete/<int:portfolio_id>')
@login_required
def delete_port(portfolio_id):
    delete_portfolio(portfolio_id)
    return redirect(url_for('.manager'))


@main.route('/projects/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ProjectForm()
    portfolio_id = session['portfolio_id']
    if form.validate_on_submit():
        if form.languages.entries:
            create_project(form=form, portfolio_id=portfolio_id)
        return redirect(url_for('.portfolio_view', portfolio_id=portfolio_id))
    return render_template('addProject.html', form=form, portfolio_id=portfolio_id)


@main.route('/projects/delete/<int:project_id>', methods=['GET'])
@login_required
def delete_prj(project_id):
    delete_project(project_id=project_id)
    return redirect(url_for('.portfolio_view', portfolio_id=session['portfolio_id']))


@main.route('/projects/edit/<int:project_id>', methods=['GET', 'POST'])
@login_required
def edit_prj(project_id):
    form = ProjectForm()
    if form.validate_on_submit():
        if form.languages.entries:
            update_project(project_id=project_id, form=form)
        return redirect(url_for('.portfolio_view', portfolio_id=session['portfolio_id']))
    return render_template('editProject.html', form=form, project_id=project_id)


@main.route('/manager')
@login_required
def manager():
    user = get_user_by_id(int(current_user.get_id()))
    return render_template('portfoliosManager.html', portfolios=user.portfolios)
