from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

<<<<<<< HEAD
class UserHashForm(FlaskForm):
    userHash = StringField('User hash', validators=[DataRequired(), Length(min=32, max=32)])
    submit = SubmitField('Submit')

class RootHashForm(FlaskForm):
    rootHash = StringField('Root hash', validators=[DataRequired, Length(min=32, max=32)])
=======
class SubmitHashForm(FlaskForm):
    hash = StringField('Hash',
                        validators=[DataRequired(), Length(min=5, max=20)])
>>>>>>> dedbd463cf91e2bb398bf5042472d3f62a3dc422
    submit = SubmitField('Submit')