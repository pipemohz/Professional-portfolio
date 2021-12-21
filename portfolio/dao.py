from portfolio import db
from portfolio.models.language import Language
from portfolio.models.project import Project
from portfolio.forms.forms import ProjectForm


def get_projects():
    return db.session.query(Project).all()


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
                name=entry.data
            )

        project.languages.append(language)

    db.session.add(project)
    db.session.commit()
