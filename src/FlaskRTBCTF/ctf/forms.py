from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, RadioField
from wtforms.validators import (
    DataRequired,
    Length,
    ValidationError,
    IPAddress,
    NumberRange,
    AnyOf,
)
from wtforms.fields.html5 import IntegerField
from wtforms.widgets import HiddenInput, SubmitInput
from .models import Machine, Challenge


class MachineForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=4, max=32)])
    os = RadioField(
        "Operating System of machine",
        validators=[DataRequired()],
        choices=(("linux", "Linux"), ("windows", "Windows"), ("android", "Android")),
    )
    user_hash = StringField(
        "User Hash", validators=[DataRequired(), Length(min=32, max=32)]
    )
    root_hash = StringField(
        "Root Hash", validators=[DataRequired(), Length(min=32, max=32)]
    )
    user_points = IntegerField("Points for User Hash", validators=[DataRequired()])
    root_points = IntegerField("Points for Root Hash", validators=[DataRequired()])
    ip = StringField(
        "IPv4 address of machine", validators=[DataRequired(), IPAddress()]
    )
    difficulty = RadioField(
        "Difficuly Level",
        validators=[DataRequired()],
        choices=(
            ("easy", "Easy"),
            ("medium", "Medium"),
            ("hard", "Hard"),
            ("insane", "Insane"),
        ),
    )

    submit = SubmitField("Submit")


class UserHashForm(FlaskForm):
    machine_id = HiddenField("Machine ID", validators=[DataRequired()])
    user_hash = StringField(
        "User Hash", validators=[DataRequired(), Length(min=32, max=32)]
    )
    submit_user_hash = SubmitField("Submit")

    def validate_machine_id(self, machine_id):
        if (machine_id == "") or (machine_id is None):
            raise ValidationError(
                "Server Error. Please hard refresh the page and try again."
            )

    def validate_user_hash(self, user_hash):
        box = Machine.query.get(int(self.machine_id.data))
        if not box:
            raise ValidationError("No machine with that ID exists")
        elif box.user_hash != str(user_hash.data):
            raise ValidationError("Incorrect User Hash")


class RootHashForm(FlaskForm):
    machine_id = HiddenField("Machine ID", validators=[DataRequired()])
    root_hash = StringField(
        "Root Hash", validators=[DataRequired(), Length(min=32, max=32)]
    )
    submit_root_hash = SubmitField("Submit")

    def validate_machine_id(self, machine_id):
        if (machine_id == "") or (machine_id is None):
            raise ValidationError(
                "Server Error. Please hard refresh the page and try again."
            )

    def validate_root_hash(self, root_hash):
        box = Machine.query.get(int(self.machine_id.data))
        if not box:
            raise ValidationError("No machine with that ID exists")
        elif box.root_hash == str(root_hash.data):
            pass
        else:
            raise ValidationError("Incorrect Root Hash.")


class ChallengeFlagForm(FlaskForm):
    challenge_id = HiddenField("Challenge ID", validators=[DataRequired()])
    flag = StringField("Flag", validators=[DataRequired(), Length(min=4)])
    submit_flag = SubmitField("Submit")

    def validate_flag(self, flag):
        ch = Challenge.query.get(int(self.challenge_id.data))
        if not ch:
            raise ValidationError("No challenge with that ID exists")
        elif ch.flag != str(flag.data):
            raise ValidationError("Incorrect flag.")


class RatingForm(FlaskForm):
    machine_challenge_id = IntegerField(
        label="ID", widget=HiddenInput(), validators=[DataRequired()]
    )
    rating_for = HiddenField(
        label="Machine or Challenge?",
        validators=[DataRequired(), AnyOf(("machine", "challenge"))],
    )
    rating_value = IntegerField(
        label="Rating",
        widget=SubmitInput(),
        validators=[DataRequired(), NumberRange(min=1, max=5)],
    )
