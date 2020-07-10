from flask import url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList
from wtforms.fields.html5 import DateField, TimeField, URLField
from wtforms.validators import DataRequired, Length, URL
from sqlalchemy.exc import SQLAlchemyError

from FlaskRTBCTF.utils import db, admin_only, cache
from .models import Settings, Website


class SettingsForm(FlaskForm):
    ctf_name = StringField(
        "CTF Name", validators=[DataRequired(), Length(min=3, max=64)]
    )
    organization_name = StringField(
        "Organization Name", validators=[DataRequired(), Length(min=3, max=80)],
    )
    from_date = DateField("Start Date", format="%Y-%m-%d")
    from_time = TimeField("Start Time")
    to_date = DateField("End Date", format="%Y-%m-%d")
    to_time = TimeField("End Time")

    submit = SubmitField("Save & Next")

    @admin_only
    def setup(self):
        if self.is_submitted():
            try:
                settings = Settings.query.get(1)

                settings.dummy = False
                settings.ctf_name = self.ctf_name.data
                settings.organization_name = self.organization_name.data
                settings.from_date = self.from_date.data
                settings.from_time = self.from_time.data
                settings.to_date = self.to_date.data
                settings.to_time = self.to_time.data

                db.session.commit()

                cache.delete(key="past_running_time")
                cache.delete(key="settings")
                step = 3

            except SQLAlchemyError:
                db.session.rollback()
                flash("Transaction failed. Please try again.", "danger")
                step = 2

        else:
            flash("Form validation failed. Please try again.", "danger")
            step = 2

        return redirect(url_for("main.setup", step=step))


class WebsiteForm(FlaskForm):
    names = FieldList(
        StringField("Label", validators=[DataRequired(), Length(min=2, max=64)]),
        min_entries=1,
        max_entries=3,
    )
    urls = FieldList(
        URLField("URL", validators=[DataRequired(), URL()]),
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
                    obj = Website(name=w[0], url=w[1])
                    db.session.add(obj)
                db.session.commit()
                cache.delete(key="websites")
                flash(
                    "CTF setup was successful! \
                        You can use admin controls for managing database tables.",
                    "success",
                )
                return redirect(url_for("main.home"))

            except SQLAlchemyError:
                db.session.rollback()
                flash("Transaction failed. Please try again.", "danger")

        else:
            flash("Error: Couldn't save form data.", "danger")

        return redirect(url_for("main.setup", step=3))
