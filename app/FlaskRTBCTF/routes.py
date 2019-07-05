''' views / routes '''

from flask import render_template, url_for, flash, redirect, request
from FlaskRTBCTF import app, db, bcrypt
from FlaskRTBCTF.forms import RegistrationForm, LoginForm, UserHashForm, RootHashForm
from FlaskRTBCTF.models import User, Score
from flask_login import login_user, current_user, logout_user, login_required
from FlaskRTBCTF.config import ctfname, userHash, rootHash, userScore, rootScore
from datetime import datetime

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', ctfname=ctfname)

''' Scoreboard and machine info '''

@app.route("/scoreboard")
@login_required
def scoreboard():
    users = User.query.order_by(User.id).all()
    scores = Score.query.order_by(Score.score.desc(), Score.timestamp).all()
    userNameScoreList = []
    for score in scores:
        userNameScoreList.append({'username':users[score.userid-1].username,'score':score.score})
    return render_template('scoreboard.html', scores=userNameScoreList, ctfname=ctfname)


''' Hash Submission Management '''

@app.route("/machine", methods=['GET', 'POST'])
@login_required
def machine():
    userHashForm = UserHashForm()
    rootHashForm = RootHashForm()
    return render_template('machine.html', userHashForm=userHashForm,
                           rootHashForm=rootHashForm, ctfname=ctfname)


@login_required
@app.route("/validateRootHash", methods=['POST'])
def validateRootHash():
    rootHashForm = RootHashForm()
    if rootHashForm.validate_on_submit():
        if rootHashForm.rootHash.data == rootHash:
            score = Score.query.get(current_user.id)
            if score.rootHash:
                flash("You already own System.", "success")
            else:
                score.rootHash = True
                score.score += rootScore
                score.timestamp = datetime.utcnow()
                db.session.commit()
                flash("Congrats! correct system hash.", "success")
        else:
            flash("Sorry! Wrong system hash", "danger")
        return redirect(url_for('machine'))
    else:
        return redirect(url_for('machine'))


@login_required
@app.route("/validateUserHash", methods=['POST'])
def validateUserHash():
    userHashForm = UserHashForm()
    if userHashForm.validate_on_submit():
        if userHashForm.userHash.data == userHash:
            score = Score.query.get(current_user.id)
            if score.userHash:
                flash("You already own User.", "success")
            else:
                score.userHash = True
                score.score += userScore
                score.timestamp = datetime.utcnow()
                db.session.commit()
                flash("Congrats! correct user hash.", "success")
        else:
            flash("Sorry! Wrong user hash", "danger")
        return redirect(url_for('machine'))
    else:
        return redirect(url_for('machine'))


''' Register/login/logout/account management '''


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('Already Authenticated', 'info')
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() or User.query.filter_by(email=form.email.data).first()
        if user:
            flash("User with same username or email already exists!", "danger")
            return redirect(url_for('register'))
        else:
            hashed_password = bcrypt.generate_password_hash(
                form.password.data).decode('utf-8')
            user = User(username=form.username.data,
                        email=form.email.data, password=hashed_password)
            score = Score(userid=user.id, userHash=False, rootHash=False, score=0)
            db.session.add(user)
            db.session.add(score)
            db.session.commit()
            flash('Your account has been created! You are now able to log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form, ctfname=ctfname)


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
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form, ctfname=ctfname)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.", "info")
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account', ctfname=ctfname)


