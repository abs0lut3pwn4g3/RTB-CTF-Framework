''' views / routes '''

from flask import Blueprint, render_template, flash
from flask_login import current_user, login_required
from FlaskRTBCTF import db, bcrypt
from FlaskRTBCTF.models import User, Score
from FlaskRTBCTF.ctf.forms import UserHashForm, RootHashForm
from FlaskRTBCTF.config import organization, box, userHash, rootHash, userScore, rootScore
from datetime import datetime

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
    userHashForm = UserHashForm()
    rootHashForm = RootHashForm()
    return render_template('machine.html', userHashForm=userHashForm,
                           rootHashForm=rootHashForm, organization=organization, box=box)

''' Hash Submission Management '''

@ctf.route("/validateRootHash", methods=['POST'])
@login_required
def validateRootHash():
    userHashForm = UserHashForm()
    rootHashForm = RootHashForm()
    if rootHashForm.validate_on_submit():
        if rootHashForm.rootHash.data == rootHash:
            score = Score.query.get(current_user.id)
            if score.rootHash:
                flash("You already own System.", "success")
            else:
                score.rootHash = True
                score.points += rootScore
                score.timestamp = datetime.utcnow()
                db.session.commit()
                flash("Congrats! correct system hash.", "success")
        else:
            flash("Sorry! Wrong system hash", "danger")
        return render_template('machine.html', userHashForm=userHashForm,
                           rootHashForm=rootHashForm, organization=organization, box=box)
    else:
        return render_template('machine.html', userHashForm=userHashForm,
                           rootHashForm=rootHashForm, organization=organization, box=box)


@ctf.route("/validateUserHash", methods=['POST'])
@login_required
def validateUserHash():
    userHashForm = UserHashForm()
    rootHashForm = RootHashForm()
    if userHashForm.validate_on_submit():
        if userHashForm.userHash.data == userHash:
            score = Score.query.get(current_user.id)
            if score.userHash:
                flash("You already own User.", "success")
            else:
                score.userHash = True
                score.points += userScore
                score.timestamp = datetime.utcnow()
                db.session.commit()
                flash("Congrats! correct user hash.", "success")
        else:
            flash("Sorry! Wrong user hash", "danger")
        return render_template('machine.html', userHashForm=userHashForm,
                           rootHashForm=rootHashForm, organization=organization, box=box)
    else:
        return render_template('machine.html', userHashForm=userHashForm,
                           rootHashForm=rootHashForm, organization=organization, box=box)


