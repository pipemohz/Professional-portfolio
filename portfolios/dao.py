from webbrowser import get
from portfolios import db
import portfolios
from portfolios.models.language import Language
from portfolios.models.project import Project
from portfolios.models.user import User
from portfolios.models.portfolio import Portfolio
from portfolios.forms.forms import LoginForm, PortfolioForm, ProjectForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
import datetime as dt


def create_portfolio(form: PortfolioForm, user: User):
    portfolio = Portfolio(
        title=form.title.data,
        description=form.description.data,
        date_created=dt.datetime.now().date(),
        date_modified=dt.datetime.now().date(),
        manager=user
    )

    db.session.add(portfolio)
    db.session.commit()


def get_portfolios():
    return db.session.query(Portfolio).all()


def get_portfolio_by_id(id: int):
    return db.session.query(Portfolio).get(id)


def get_projects_by_portfolio_id(id: int):
    return db.session.query(Project).filter_by(portfolio_id=id).first()


def get_user(form: LoginForm):
    return db.session.query(User).filter_by(name=form.username.data).first()


def get_user_by_id(user_id: int):
    return db.session.query(User).get(user_id)


def valid_password(user: User, password: str):
    return check_password_hash(user.password, password)


def language_exists(name: str):
    return db.session.query(Language).filter_by(name=name.lower()).first()


def create_project(form: ProjectForm, portfolio_id: int):
    project = Project(
        title=form.title.data,
        description=form.description.data,
        url=form.url.data,
        portfolio=get_portfolio_by_id(portfolio_id)
    )
    for entry in form.languages.entries:
        if language_exists(entry.data):
            language = language_exists(entry.data)

        else:
            language = Language(
                name=entry.data.lower()
            )

        project.languages.append(language)

    db.session.add(project)
    portfolio = get_portfolio_by_id(portfolio_id)
    portfolio.date_modified = dt.datetime.now().date()
    db.session.commit()


def delete_project(project_id: int):
    project = db.session.query(Project).get(project_id)
    db.session.delete(project)
    db.session.commit()


def create_user(form: RegisterForm):
    user = User(
        name=form.username.data,
        email=form.email.data,
        password=generate_password_hash(
            password=form.password.data, method='pbkdf2:sha256', salt_length=8)
    )

    db.session.add(user)
    db.session.commit()


def update_project(project_id: int, form: ProjectForm):
    project = db.session.query(Project).get(project_id)
    project.title = form.title.data
    project.description = form.description.data
    project.url = form.url.data

    delete_project_languages(project=project)

    for entry in form.languages.entries:
        if language_exists(entry.data):
            language = language_exists(entry.data)
        else:
            language = Language(
                name=entry.data.lower()
            )

        project.languages.append(language)

    portfolio = get_portfolio_by_id(project.portfolio_id)
    portfolio.date_modified = dt.datetime.now().date()
    db.session.commit()


def delete_project_languages(project: Project):
    for language in project.languages:
        project.languages.remove(language)


def delete_portfolio(portfolio_id: int):
    portfolio = get_portfolio_by_id(portfolio_id)

    for project in portfolio.projects:
        delete_project_languages(project)

    db.session.delete(portfolio)
    db.session.commit()
