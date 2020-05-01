from flask import render_template, Blueprint, redirect, url_for, request

from .models import Notification, Settings, Website
from .forms import SettingsForm, WebsiteForm
from FlaskRTBCTF.utils import admin_only

main = Blueprint("main", __name__)


""" Index page """


@main.route("/")
@main.route("/home")
def home():
    settings = Settings.get_settings()
    running_time = {
        "from": settings.running_time_from,
        "to": settings.running_time_to,
    }

    return render_template("home.html", RunningTime=running_time)


@main.route("/notifications")
def notifications():
    notifs = Notification.query.order_by(Notification.updated_on.desc()).all()

    return render_template("notifications.html", title="Notifications", notifs=notifs)


@main.route("/setup", methods=["GET", "POST"])
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

        if step == 2 and settings_form.validate_on_submit():
            return settings_form.setup()
        elif step == 3:
            return website_form.setup()
        else:
            return redirect(url_for("main.setup"))
