from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.core import FieldList, FormField
from wtforms.validators import URL, DataRequired
from flask_ckeditor import CKEditorField

class ProjectForm(FlaskForm):
    title = StringField(label="Project title", validators=[DataRequired()])
    description = StringField(label="Project description", validators=[DataRequired()])
    url = StringField(label="URL", validators=[DataRequired(), URL()])
    languages = FieldList(StringField(validators=[DataRequired()]), min_entries=0)
    submit = SubmitField("Create project")
    