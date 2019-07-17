from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo

class TitleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Change Title')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message')
    submit = SubmitField('Send Message', validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    age = IntegerField('Age')
    bio = TextAreaField('Biography')
    url = StringField('Profile Picture URL')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-type Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class PostForm(FlaskForm):
    tweet = StringField('What are you up to', validators=[DataRequired()])
    submit = SubmitField('Tweet')
