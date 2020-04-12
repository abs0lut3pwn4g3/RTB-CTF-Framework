from flask import render_template, Blueprint
from FlaskRTBCTF.config import organization, RunningTime
from FlaskRTBCTF.models import Notification

main = Blueprint('main', __name__)

''' Index page '''


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', organization=organization,
                           RunningTime=RunningTime)


@main.route("/notifications")
def notifications():
    notifs = Notification.query.order_by(Notification.timestamp.desc()).all()
    return render_template('notifications.html', organization=organization,
                           title="Notifications", notifs=notifs)
