from flask import render_template, Blueprint, redirect, url_for, request, flash
from flask_login import login_required

from .models import Notification, Settings, Website
from .forms import SettingsForm, WebsiteForm
from FlaskRTBCTF.utils import admin_only

main = Blueprint("main", __name__)


""" Index page """


@main.before_request
def needs_setup():
    settings = Settings.query.get(1)
    if settings.dummy:
        if request.endpoint not in ("main.setup", "users.login"):
            flash("Please setup the CTF, before accessing any routes.", "info")
            return redirect(url_for("main.setup"))
    else:
        return


@main.route("/")
@main.route("/home")
def home():
    settings = Settings.query.get(1)
    running_time = {
        "from": settings.running_time_from,
        "to": settings.running_time_to,
    }

    return render_template("home.html", RunningTime=running_time)


@main.route("/notifications")
def notifications():
    notifs = Notification.query.order_by(Notification.timestamp.desc()).all()

    return render_template("notifications.html", title="Notifications", notifs=notifs)


@main.route("/setup", methods=["GET", "POST"])
@login_required
@admin_only
def setup():
    website_form_data = {"names": list(), "urls": list()}
    for w in Website.query.all():
        website_form_data["names"].append(w.name)
        website_form_data["urls"].append(w.url)

    settings_form_data = Settings.query.get(1)

    settings_form = SettingsForm(obj=settings_form_data)
    website_form = WebsiteForm(data=website_form_data)

    if request.method == "GET":
        return render_template(
            "setup.html",
            title="Setup",
            settingsForm=settings_form,
            websitesForm=website_form,
        )

    else:

        step = int(request.args.get("step", 2))

        if step == 2:
            return settings_form.setup()
        elif step == 3:
            return website_form.setup()
        else:
            return redirect(url_for("main.setup"))
