''' views / routes ''' 

from flask import render_template, url_for, flash, redirect, request
from FlaskRTBCTF import app, db, bcrypt
from FlaskRTBCTF.forms import RegistrationForm, LoginForm, UserHashForm, RootHashForm
from FlaskRTBCTF.models import User
from flask_login import login_user, current_user, logout_user, login_required
from FlaskRTBCTF.config import ctfname

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', ctfname=ctfname)

@app.route("/scoreboard")
@login_required
def machine():
    users_sorted_by_score = User.query.order_by(User.score).all()
    return render_template('scoreboard.html', users=users_sorted_by_score, ctfname=ctfname)


''' Register/login/logout management '''


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form, ctfname=ctfname)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form, ctfname=ctfname)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account', ctfname=ctfname)

@app.route("/submit",methods=['GET','POST'])
@login_required
def submit():
    userHashForm=UserHashForm()
    rootHashForm=RootHashForm()
    if request.method=='POST':
        flash('Correct hash','success')
        return redirect(url_for('submit'))
    else:
        return render_template('submit.html', ctfname=ctfname, 
                                userHashForm=userHashForm, rootHashForm=rootHashForm)