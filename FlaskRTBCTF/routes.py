''' views / routes ''' 

from flask import render_template, url_for, flash, redirect, request
from FlaskRTBCTF import app, db, bcrypt
from FlaskRTBCTF.forms import RegistrationForm, LoginForm, SubmitHashForm
from FlaskRTBCTF.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/machine", methods=['GET', 'POST'])
def machine():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    users_sorted_by_score = User.query.order_by(User.score).all()
    form = SubmitHashForm()
    if form.validate_on_submit():
        if form.hash.data == 'root-hash-xxx-xxxx':
            flash('Correct Hash, congrats!', 'success')
            current_user.score = current_user.score+50
            db.session.commit()
        else:
            flash('Wrong Hash', 'danger')
    return render_template('machine.html', users=users_sorted_by_score, form=form)


''' Register/login/logout management '''


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('Already Authenticated', 'info')
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Already Authenticated', 'info')
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
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')