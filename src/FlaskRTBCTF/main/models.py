""" Main Application Models. """


from datetime import datetime, date, time, timedelta

from sqlalchemy.ext.hybrid import hybrid_property

from FlaskRTBCTF.utils.models import db, TimeMixin, ReprMixin
from FlaskRTBCTF.utils.cache import cache


# Notifications Model
class Notification(TimeMixin, ReprMixin, db.Model):
    __tablename__ = "notification"
    __repr_fields__ = ("title",)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.TEXT(), nullable=False)


# Settings Model
class Settings(ReprMixin, db.Model):
    __tablename__ = "settings"
    __repr_fields__ = ("ctf_name", "organization_name")
    id = db.Column(db.Integer, primary_key=True)
    dummy = db.Column(db.Boolean, nullable=False, default=True)
    ctf_name = db.Column(db.String(64), nullable=False, default="RootTheBox CTF")
    organization_name = db.Column(
        db.String(80), nullable=False, default="Abs0lut3Pwn4g3"
    )

    from_date = db.Column(db.Date, nullable=True, default=date.today())
    from_time = db.Column(db.Time, nullable=True, default=time())
    to_date = db.Column(
        db.Date, nullable=False, default=date.today() + timedelta(days=2)
    )
    to_time = db.Column(db.Time, nullable=False, default=time())

    @staticmethod
    @cache.cached(timeout=3600 * 6, key_prefix="settings")
    def get_settings():
        return Settings.query.get(1)

    @hybrid_property
    def running_time_from(self):
        return datetime.combine(self.from_date, self.from_time)

    @hybrid_property
    def running_time_to(self):
        return datetime.combine(self.to_date, self.to_time)


# Websites Model
class Website(ReprMixin, db.Model):
    __tablename__ = "website"
    __repr_fields__ = ("id", "name", "url")
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(
        db.TEXT(),
        nullable=False,
        default="https://github.com/Abs0lut3Pwn4g3/RTB-CTF-Framework",
    )
    name = db.Column(db.TEXT(), nullable=False, default="Source code on GitHub")

    @staticmethod
    @cache.cached(timeout=3600 * 6, key_prefix="websites")
    def get_websites():
        return Website.query.all()
