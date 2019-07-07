from flask import render_template, Blueprint
from FlaskRTBCTF.config import ctfname, RunningTime
import json

main = Blueprint('main', __name__)

''' Index page '''

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', ctfname=ctfname, RunningTime=json.loads(RunningTime))