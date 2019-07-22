from flask import render_template, Blueprint
from FlaskRTBCTF.config import ctfname, RunningTime
from FlaskRTBCTF.models import Notification

main = Blueprint('main', __name__)

''' Index page '''

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', ctfname=ctfname, RunningTime=RunningTime)

@main.route("/notifications")
def notifications():
    notifs = Notification.query.order_by(Notification.timestamp.desc()).all()
    return render_template('notifications.html', ctfname=ctfname, title="Notifications", notifs=notifs)