""" views / routes. """


from datetime import datetime

from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from FlaskRTBCTF.users.models import User, Logs
from FlaskRTBCTF.utils import (
    db,
    cache,
    is_past_running_time,
    admin_only,
    clear_points_cache,
    clear_rating_cache,
)
from .models import Machine, Category, UserChallenge, UserMachine
from .forms import (
    UserHashForm,
    RootHashForm,
    MachineForm,
    ChallengeFlagForm,
    RatingForm,
)


ctf = Blueprint("ctf", __name__)


# Scoreboard
@ctf.route("/scoreboard")
@cache.cached(timeout=120, key_prefix="scoreboard")
def scoreboard():
    usersScores = User.get_all()
    usersScores.sort(reverse=True, key=lambda user: user.points(id=user.id))

    return render_template("scoreboard.html", scores=usersScores)


# Machines Info
@ctf.route("/machines", methods=["GET", "POST"])
@login_required
def machines():
    userHashForm = UserHashForm()
    rootHashForm = RootHashForm()
    ratingForm = RatingForm()

    is_finished = is_past_running_time()

    if request.method == "GET":
        boxes = Machine.get_all()
        completed = UserMachine.completed_machines(user_id=current_user.id)
        rated = UserMachine.rated_machines(user_id=current_user.id)

        log = Logs.query.get(current_user.id)
        # check if it is the first visit to machine page for user
        if log.visitedMachine is False:
            log.visitedMachine = True
            log.machineVisitTime = datetime.utcnow()
            db.session.commit()

        return render_template(
            "machines.html",
            boxes=boxes,
            completed=completed,
            rated=rated,
            is_finished=is_finished,
            userHashForm=userHashForm,
            rootHashForm=rootHashForm,
            ratingForm=ratingForm,
        )

    else:
        if is_finished:
            flash("Sorry! CTF has ended.", "danger")
            return redirect(url_for("ctf.machines"))

        machine_id = int(userHashForm.machine_id.data or rootHashForm.machine_id.data)
        user_machine = UserMachine.query.filter_by(
            user_id=current_user.id, machine_id=machine_id
        ).first()

        if not user_machine:
            user_machine = UserMachine(user_id=current_user.id, machine_id=machine_id)
            db.session.add(user_machine)
            db.session.commit()

        if userHashForm.submit_user_hash.data and userHashForm.validate_on_submit():
            if user_machine.owned_user:
                flash("You already own User.", "success")
                return redirect(url_for("ctf.machines"))

            user_machine.owned_user = True
            log = Logs.query.get(current_user.id)
            log.userSubmissionIP = request.access_route[0]
            log.userSubmissionTime = datetime.utcnow()
            log.userOwnTime = str(log.userSubmissionTime - log.machineVisitTime)
            db.session.commit()
            clear_points_cache(userId=current_user.id, mode="m")
            flash("Congrats! correct user hash.", "success")

        elif rootHashForm.submit_root_hash.data and rootHashForm.validate_on_submit():
            if user_machine.owned_root:
                flash("You already own System.", "success")
                return redirect(url_for("ctf.machines"))

            user_machine.owned_root = True
            log = Logs.query.get(current_user.id)
            log.rootSubmissionIP = request.access_route[0]
            log.rootSubmissionTime = datetime.utcnow()
            log.rootOwnTime = str(log.rootSubmissionTime - log.machineVisitTime)
            db.session.commit()
            clear_points_cache(userId=current_user.id, mode="m")
            flash("Congrats! correct root hash.", "success")

        else:
            errors = userHashForm.user_hash.errors or rootHashForm.root_hash.errors
            for e in errors:
                flash(e, "danger")

        return redirect(url_for("ctf.machines"))


# New machine form
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


# Edit machine form
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


# Challenges Info
@ctf.route("/challenges", methods=["GET", "POST"])
@login_required
def challenges():
    flagForm = ChallengeFlagForm()
    ratingForm = RatingForm()

    if request.method == "GET":
        categories_challenges = Category.get_challenges()
        completed = UserChallenge.completed_challenges(user_id=current_user.id)
        rated = UserChallenge.rated_challenges(user_id=current_user.id)

        return render_template(
            "challenges.html",
            is_finished=is_past_running_time(),
            categories=categories_challenges,
            completed=completed,
            rated=rated,
            chalFlagForm=flagForm,
            chalRatingForm=ratingForm,
        )

    else:
        if is_past_running_time():
            flash("Sorry! CTF has ended.", "danger")

        elif flagForm.validate_on_submit():
            ch_id = int(flagForm.challenge_id.data)
            user_ch = UserChallenge.query.filter_by(
                user_id=current_user.id, challenge_id=ch_id
            ).first()

            if not user_ch:
                user_ch = UserChallenge(user_id=current_user.id, challenge_id=ch_id)
                db.session.add(user_ch)
            elif user_ch.completed:
                flash(
                    "You've already submitted the flag for this challenge.", "success"
                )
                return redirect(request.url)

            user_ch.completed = True
            db.session.commit()
            clear_points_cache(userId=current_user.id, mode="c")
            flash("Congrats! correct flag.", "success")

        else:
            flash(flagForm.errors, "danger")

        return redirect(url_for("ctf.challenges"))


# Rating Form Submit
@ctf.route("/submit_rating", methods=("POST",))
@login_required
def submit_rating():
    form = RatingForm()
    if form.validate_on_submit():
        if form.rating_for.data == "machine":
            try:
                user_machine = UserMachine.query.get(
                    {
                        "user_id": current_user.id,
                        "machine_id": form.machine_challenge_id.data,
                    }
                )
                if (
                    user_machine
                    and user_machine.owned_user
                    and user_machine.owned_root
                    and user_machine.rating == 0
                ):
                    user_machine.rating = form.rating_value.data
                    db.session.commit()
                    clear_rating_cache(
                        user_id=current_user.id, machine_id=user_machine.machine_id
                    )
                    flash("Thank you for rating!", "success")
                elif user_machine.rating != 0:
                    flash("You can only rate once", "danger")
                else:
                    flash(
                        "You can rate only after you own both System and User", "danger"
                    )
            except Exception as e:
                flash(str(e), "danger")

            return redirect(url_for("ctf.machines"))

        elif form.rating_for.data == "challenge":
            try:
                user_ch = UserChallenge.query.get(
                    {
                        "user_id": current_user.id,
                        "challenge_id": form.machine_challenge_id.data,
                    }
                )
                if user_ch.completed and user_ch.rating == 0:
                    user_ch.rating = form.rating_value.data
                    db.session.commit()
                    clear_rating_cache(
                        user_id=current_user.id, ch_id=user_ch.challenge_id
                    )
                    flash("Thank you for rating!", "success")
                elif user_ch.rating != 0:
                    flash("You can only rate once", "danger")
                elif not user_ch.completed:
                    flash("You can rate only after submitting flag", "danger")
            except Exception as e:
                flash(str(e), "danger")

            return redirect(url_for("ctf.challenges"))
    else:
        flash(form.errors, "danger")
        return redirect(url_for("main.home"))
