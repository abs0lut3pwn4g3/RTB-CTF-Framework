''' views / routes '''

from flask import Blueprint, render_template, flash, request
from flask_login import current_user, login_required
from FlaskRTBCTF import db, bcrypt
from FlaskRTBCTF.config import organization, box, userHash, rootHash, userScore, rootScore, LOGGING, RunningTime
from FlaskRTBCTF.models import User, Score
if LOGGING:
    from FlaskRTBCTF.models import Logs
from FlaskRTBCTF.ctf.forms import UserHashForm, RootHashForm
from datetime import datetime
import pytz

ctf = Blueprint('ctf', __name__)


''' Scoreboard '''

@ctf.route("/scoreboard")
@login_required
def scoreboard():
    scores = Score.query.order_by(Score.points.desc(), Score.timestamp).all()
    userNameScoreList = []
    for score in scores:
        userNameScoreList.append({'username': User.query.get(score.user_id).username,'score':score.points})

    return render_template('scoreboard.html', scores=userNameScoreList, organization=organization)


''' Machine Info '''

@ctf.route("/machine")
@login_required
def machine():
    user = User.query.get(current_user.id)
    if LOGGING:
        log = Logs.query.get(current_user.id)
        if log.visitedMachine is False:
            log.visitedMachine = True
            log.machineVisitTime = datetime.utcnow()
            db.session.commit()
    userHashForm = UserHashForm()
    rootHashForm = RootHashForm()
    end_date_time = RunningTime["to"]
    current_date_time = datetime.now(pytz.utc)
    return render_template('machine.html', userHashForm=userHashForm,
                           rootHashForm=rootHashForm, organization=organization, box=box, current=current_date_time, end=end_date_time)

''' Hash Submission Management '''

@ctf.route("/validateRootHash", methods=['POST'])
@login_required
def validateRootHash():
    userHashForm = UserHashForm()
    rootHashForm = RootHashForm()
    end_date_time = RunningTime["to"]
    current_date_time = datetime.now(pytz.utc)
    if rootHashForm.validate_on_submit():    
        if current_date_time > end_date_time:
            flash("Sorry! Contest has ended", "danger")
        elif rootHashForm.rootHash.data == rootHash:
            score = Score.query.get(current_user.id)
            if score.rootHash:
                flash("You already own System.", "success")
            else:
                score.rootHash = True
                score.points += rootScore
                score.timestamp = datetime.utcnow()
                if LOGGING:
                    log = Logs.query.get(current_user.id)
                    log.rootSubmissionIP = request.access_route[0]
                    log.rootSubmissionTime = datetime.utcnow()
                    log.rootOwnTime = str(log.rootSubmissionTime - log.machineVisitTime)
                db.session.commit()
                flash("Congrats! correct system hash.", "success")
        else:
            flash("Sorry! Wrong system hash", "danger")
        return render_template('machine.html', userHashForm=userHashForm,
                           rootHashForm=rootHashForm, organization=organization, box=box, current=current_date_time, end=end_date_time)
    else:
        return render_template('machine.html', userHashForm=userHashForm,
                           rootHashForm=rootHashForm, organization=organization, box=box, current=current_date_time, end=end_date_time)


@ctf.route("/validateUserHash", methods=['POST'])
@login_required
def validateUserHash():
    userHashForm = UserHashForm()
    rootHashForm = RootHashForm()
    end_date_time = RunningTime["to"]
    current_date_time = datetime.now(pytz.utc)
    if userHashForm.validate_on_submit():    
        if current_date_time > end_date_time:
            flash("Sorry! Contest has ended", "danger")
        elif userHashForm.userHash.data == userHash:
            score = Score.query.get(current_user.id)
            if score.userHash:
                flash("You already own User.", "success")
            else:
                score.userHash = True
                score.points += userScore
                score.timestamp = datetime.utcnow()
                if LOGGING:
                    log = Logs.query.get(current_user.id)
                    log.userSubmissionIP = request.access_route[0]
                    log.userSubmissionTime = datetime.utcnow()
                    log.userOwnTime = str(log.userSubmissionTime - log.machineVisitTime)
                db.session.commit()
                flash("Congrats! correct user hash.", "success")
        else:
            flash("Sorry! Wrong user hash", "danger")
        return render_template('machine.html', userHashForm=userHashForm,
                           rootHashForm=rootHashForm, organization=organization, box=box, current=current_date_time, end=end_date_time)
    else:
        return render_template('machine.html', userHashForm=userHashForm,
                           rootHashForm=rootHashForm, organization=organization, box=box, current=current_date_time, end=end_date_time)


