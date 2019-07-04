''' views / routes ''' 

from flask import render_template, url_for, flash, redirect
from FlaskRTBCTF import app
from FlaskRTBCTF.forms import RegistrationForm, LoginForm
from FlaskRTBCTF.models import User

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/machine")
def machine():
    return render_template('machine.html')


''' Register/login/logout management '''

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@FlaskRTBCTF.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)