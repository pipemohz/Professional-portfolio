from portfolio import db
from portfolio.models.language import Language
from portfolio.models.project import Project
from portfolio.models.user import User
from portfolio.forms.forms import LoginForm, ProjectForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash


def get_projects():
    return db.session.query(Project).all()


def get_user(form: LoginForm):
    return db.session.query(User).filter_by(name=form.username.data).first()


def valid_password(user: User, password: str):
    return check_password_hash(user.password, password)


def language_exists(name: str):
    return db.session.query(Language).filter_by(name=name.lower()).first()


def create_project(form: ProjectForm):
    project = Project(
        title=form.title.data,
        description=form.description.data,
        url=form.url.data
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

    for entry in form.languages.entries:
        if language_exists(entry.data):
            language = language_exists(entry.data)
        else:
            language = Language(
                name=entry.data.lower()
            )

        project.languages.append(language)

    db.session.commit()
