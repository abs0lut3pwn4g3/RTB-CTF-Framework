from flask import url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SubmitField, FieldList
from wtforms.widgets.html5 import URLInput, DateInput, TimeInput
from wtforms.validators import DataRequired, Length, URL
from sqlalchemy.exc import SQLAlchemyError

from FlaskRTBCTF import db
from FlaskRTBCTF.utils import admin_only
from .models import Settings, Website


class SettingsForm(FlaskForm):
    ctf_name = StringField(
        "CTF Name", validators=[DataRequired(), Length(min=3, max=64)]
    )
    organization_name = StringField(
        "Organization Name", validators=[DataRequired(), Length(min=3, max=80)],
    )
    from_date = DateField("Start Date", format="%Y-%m-%d", widget=DateInput())
    from_time = TimeField("Start Time", widget=TimeInput())
    to_date = DateField("End Date", format="%Y-%m-%d", widget=DateInput())
    to_time = TimeField("End Time", widget=TimeInput())

    submit = SubmitField("Next")

    @admin_only
    def setup(self):
        if self.is_submitted():
            settings = Settings.query.get(1)

            settings.ctf_name = self.ctf_name.data
            settings.organization_name = self.organization_name.data
            settings.from_date = self.from_date.data
            settings.from_time = self.from_time.data
            settings.to_date = self.to_date.data
            settings.to_time = self.to_time.data
            settings.dummy = False

            db.session.commit()

            return redirect(url_for("main.setup", step=3))
        else:
            return redirect(url_for("main.setup", step=2))


class WebsiteForm(FlaskForm):
    names = FieldList(
        StringField("Label", validators=[DataRequired(), Length(min=2, max=64)]),
        min_entries=1,
        max_entries=3,
    )
    urls = FieldList(
        StringField("URL", validators=[DataRequired(), URL()], widget=URLInput()),
        min_entries=1,
        max_entries=3,
    )
    submit = SubmitField("Finish Setup")

    @admin_only
    def setup(self):
        if self.is_submitted():
            try:
                Website.query.delete()
                for w in zip(self.names.data, self.urls.data):
                    obj = Website(settings_id=1, name=w[0], url=w[1])
                    db.session.add(obj)
                db.session.commit()
                flash(
                    "CTF setup was successful! \
                        You can use admin controls for managing database tables.",
                    "success",
                )
                return redirect(url_for("main.home"))

            except SQLAlchemyError:
                db.session.rollback()
                flash("Transaction failed. Please try again.", "danger")
                return redirect(url_for("main.setup"), step=3)

        else:
            flash("Error: Couldn't save form data.", "danger")
            return redirect(url_for("main.setup", step=3))
