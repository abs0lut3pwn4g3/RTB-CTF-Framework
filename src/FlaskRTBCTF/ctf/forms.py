from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError
from .models import Machine


class UserHashForm(FlaskForm):
    machine_id = HiddenField("Machine ID", validators=[DataRequired()])
    user_hash = StringField(
        "User Hash", validators=[DataRequired(), Length(min=32, max=32)]
    )
    submit_user_hash = SubmitField("Submit")

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

    def validate_root_hash(self, root_hash):
        box = Machine.query.get(int(self.machine_id.data))
        if not box:
            raise ValidationError("No machine with that ID exists")
        elif box.user_hash == str(root_hash.data):
            pass
        else:
            raise ValidationError("Incorrect Root Hash.")
