""" views / routes. """


from datetime import datetime

from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required

from FlaskRTBCTF import db
from FlaskRTBCTF.users.models import User, Logs
from FlaskRTBCTF.utils import is_past_running_time
from .models import Machine
from .forms import UserHashForm, RootHashForm


ctf = Blueprint("ctf", __name__)


# context processor


@ctf.context_processor
def inject_context():
    boxes = Machine.query.all()
    past_running_time = is_past_running_time()

    return dict(boxes=boxes, past_running_time=past_running_time)


# Scoreboard


@ctf.route("/scoreboard")
@login_required
def scoreboard():
    users_score = User.query.order_by(User.points.desc()).all()
    userNameScoreList = []
    for u in users_score:
        userNameScoreList.append({"username": u.username, "score": u.points})

    return render_template("scoreboard.html", scores=userNameScoreList)


# Machines Info


@ctf.route("/machines", methods=["GET", "POST"])
@login_required
def machines():
    userHashForm = UserHashForm()
    rootHashForm = RootHashForm()

    if request.method == "GET":
        log = Logs.query.get(current_user.id)

        # check if it is the first visit to machine page for user
        if log.visitedMachine is False:
            log.visitedMachine = True
            log.machineVisitTime = datetime.utcnow()
            db.session.commit()

    else:
        if is_past_running_time():
            flash("Sorry! CTF has ended.", "danger")
            return redirect(url_for("ctf.machines"))

        """
           Todo: Get Object from UserMachine Model, dummy object given below
        """
        user_machine: object = {
            "machine_id": 1,
            "user_id": 1,
            "owned_user": False,
            "owned_root": False,
        }

        if user_machine.owned_user:
            flash("You already own User.", "success")
            return redirect(url_for("ctf.machines"))

        elif user_machine.owned_root:
            flash("You already own System.", "success")
            return redirect(url_for("ctf.machines"))

        elif userHashForm.submit_user_hash.data and userHashForm.validate_on_submit():
            box = Machine.query.get(int(userHashForm.machine_id.data))
            user_machine.owned_user = True
            current_user.points += box.user_points
            log = Logs.query.get(current_user.id)
            log.userSubmissionIP = request.access_route[0]
            log.userSubmissionTime = datetime.utcnow()
            log.userOwnTime = str(log.userSubmissionTime - log.machineVisitTime)
            db.session.commit()
            flash("Congrats! correct user hash.", "success")

        elif rootHashForm.submit_root_hash.data and rootHashForm.validate_on_submit():
            box = Machine.query.get(int(rootHashForm.machine_id.data))
            user_machine.owned_root = True
            current_user.points += box.root_points
            log = Logs.query.get(current_user.id)
            log.rootSubmissionIP = request.access_route[0]
            log.rootSubmissionTime = datetime.utcnow()
            log.rootOwnTime = str(log.rootSubmissionTime - log.machineVisitTime)
            db.session.commit()
            flash("Congrats! correct root hash.", "success")

    return render_template(
        "machine.html", userHashForm=userHashForm, rootHashForm=rootHashForm,
    )
