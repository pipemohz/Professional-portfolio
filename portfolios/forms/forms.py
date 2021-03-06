from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.core import FieldList, FormField
from wtforms.validators import URL, DataRequired, Email, Length
from flask_ckeditor import CKEditorField


class ProjectForm(FlaskForm):
    title = StringField(label="Project title", validators=[DataRequired()])
    description = StringField(
        label="Project description", validators=[DataRequired(), Length(min=5, max=255)])
    url = StringField(label="URL", validators=[DataRequired(), URL()])
    languages = FieldList(StringField(
        validators=[DataRequired()]), min_entries=0)
    submit = SubmitField("Create project")


class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[
                             DataRequired(), Length(min=5)])
    submit = SubmitField("Create user")


class LoginForm(FlaskForm):
    username = StringField(label="username", validators=[DataRequired()])
    password = PasswordField(label="password", validators=[DataRequired()])
    submit = SubmitField(label="login")


class PortfolioForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    description = StringField(label='Description', validators=[DataRequired()])
    submit = SubmitField(label='Create')


class MailForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email Address', validators=[
                        DataRequired(), Email()])
    phone = StringField(label='Phone Number', validators=[DataRequired()])
    message = CKEditorField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Send email')
