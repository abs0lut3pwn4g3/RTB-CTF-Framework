""" views / routes. """


from datetime import datetime

from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required

from FlaskRTBCTF.users.models import User, Logs
from FlaskRTBCTF.ctf.models import UserMachine
from FlaskRTBCTF.utils import db, cache, is_past_running_time, admin_only
from .models import Machine
from .forms import UserHashForm, RootHashForm, MachineForm


ctf = Blueprint("ctf", __name__)


# Scoreboard


@ctf.route("/scoreboard")
@cache.cached(timeout=120, key_prefix="scoreboard")
def scoreboard():
    users_scores = (
        User.query.with_entities(User.username, User.points)
        .order_by(User.points.desc())
        .all()
    )

    return render_template("scoreboard.html", scores=users_scores)


# Machines Info


@ctf.route("/machines", methods=["GET", "POST"])
@login_required
def machines():
    userHashForm = UserHashForm()
    rootHashForm = RootHashForm()

    machine_id = userHashForm.machine_id.data
    boxes = Machine.get_all()
    past_running_time = is_past_running_time()

    if request.method == "GET":

        log = Logs.query.get(current_user.id)

        # check if it is the first visit to machine page for user
        if log.visitedMachine is False:
            log.visitedMachine = True
            log.machineVisitTime = datetime.utcnow()
            db.session.commit()

    else:
        if past_running_time:
            flash("Sorry! CTF has ended.", "danger")
            return redirect(url_for("ctf.machines"))

        user_machine = UserMachine.query.filter_by(
            user_id=current_user.id, machine_id=machine_id
        ).first()

        if not user_machine:
            user_machine = UserMachine(
                user_id=current_user.id,
                machine_id=machine_id,
                owned_user=False,
                owned_root=False,
            )
            db.session.add(user_machine)

        if user_machine.owned_user:
            flash("You already own User.", "success")
            return redirect(url_for("ctf.machines"))

        elif user_machine.owned_root:
            flash("You already own System.", "success")
            return redirect(url_for("ctf.machines"))

        if userHashForm.submit_user_hash.data and userHashForm.validate_on_submit():
            box = Machine.query.get(int(userHashForm.machine_id.data))
            user_machine.owned_user = True
            current_user.points += box.user_points
            log = Logs.query.get(current_user.id)
            log.userSubmissionIP = request.access_route[0]
            log.userSubmissionTime = datetime.utcnow()
            log.userOwnTime = str(log.userSubmissionTime - log.machineVisitTime)
            db.session.commit()
            cache.delete(key="scoreboard")
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
            cache.delete(key="scoreboard")
            flash("Congrats! correct root hash.", "success")

        else:
            errors = userHashForm.user_hash.errors or rootHashForm.root_hash.errors
            for e in errors:
                flash(e, "danger")

        return redirect(url_for("ctf.machines"))

    return render_template(
        "machines.html",
        boxes=boxes,
        past_running_time=past_running_time,
        userHashForm=userHashForm,
        rootHashForm=rootHashForm,
    )


@ctf.route("/machines/new", methods=["GET", "POST"])
@admin_only
def new_machine():
    form = MachineForm(obj=Machine.query.get(1))
    if request.method == "GET":
        return render_template(
            "new_machine.html", form_title="Add New Machine", form=form
        )
    else:
        if form.validate_on_submit():
            new_machine = Machine()
            form.populate_obj(new_machine)
            db.session.add(new_machine)
            db.session.commit()
            cache.delete(key="machines")
            flash(f"{form.name.data} has been added.", "success")
            return redirect(url_for("ctf.machines"))
        else:
            flash(form.errors, "danger")
            return redirect(request.url)


@ctf.route("/machines/edit/<int:id>", methods=["GET", "POST"])
@admin_only
def edit_machine(id):
    machine = Machine.query.get_or_404(id)
    form = MachineForm(obj=machine)
    if request.method == "GET":
        return render_template(
            "new_machine.html", form_title=f"Editing machine #{id}", form=form
        )
    else:
        if form.validate_on_submit():
            form.populate_obj(machine)
            db.session.commit()
            cache.delete(key="machines")
            flash(f"{form.name.data} has been edited.", "success")
            return redirect(url_for("ctf.machines"))
        else:
            flash(form.errors, "danger")
            return redirect(request.url)
