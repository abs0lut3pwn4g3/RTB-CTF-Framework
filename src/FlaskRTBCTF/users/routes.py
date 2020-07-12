from datetime import datetime
import pytz

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from FlaskRTBCTF.utils import db, bcrypt, send_reset_email
from .forms import (
    RegistrationForm,
    LoginForm,
    RequestResetForm,
    ResetPasswordForm,
)
from .models import User, Logs


users = Blueprint("users", __name__)


""" User management """


@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("Already Authenticated.", "info")
        return redirect(url_for("main.home"))

    form = RegistrationForm()

    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
        #     "utf-8"
        # )
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        log = Logs(
            user=user,
            accountCreationTime=datetime.now(pytz.utc),
            visitedMachine=False,
            machineVisitTime=None,
            userSubmissionTime=None,
            rootSubmissionTime=None,
            userSubmissionIP=None,
            rootSubmissionIP=None,
        )

        db.session.add(log)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in.", "success")
        return redirect(url_for("users.login"))

    return render_template("register.html", title="Register", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("Already Authenticated", "info")
        return redirect(url_for("main.home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        pw_chk = bcrypt.check_password_hash(user.password, form.password.data)
        if user and pw_chk:
            login_user(user, remember=form.remember.data, force=True)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash("Login Unsuccessful. Please check username and password.", "danger")
    return render_template("login.html", title="Login", form=form)


@users.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.", "info")
    return redirect(url_for("main.home"))


@users.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")


@users.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RequestResetForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            send_reset_email(user)
            flash(
                "An email has been sent with instructions to reset your password.",
                "info",
            )
            return redirect(url_for("users.login"))
        except Exception:
            flash("Mail is not setup. Please contact admin directly.", "info")
            return redirect(request.url)
    return render_template("reset_request.html", title="Reset Password", form=form)


@users.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    user = User.verify_reset_token(token)

    if user is None:
        flash("That is an invalid or expired token", "danger")
        return redirect(url_for("users.reset_request"))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user.password = hashed_password
        db.session.commit()
        flash("Your password has been updated! You are now able to log in", "success")
        return redirect(url_for("users.login"))

    return render_template("reset_token.html", title="Reset Password", form=form)
