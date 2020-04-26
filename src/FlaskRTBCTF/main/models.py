""" Main Application Models. """


from datetime import datetime, date, time, timedelta

from sqlalchemy.ext.hybrid import hybrid_property

from FlaskRTBCTF.utils import db


# Notifications Table


class Notification(db.Model):
    __tablename__ = "notification"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.TEXT(), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Notif('{self.title}', '{self.body}')"


# Settings Table


class Settings(db.Model):
    __tablename__ = "settings"
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

    websites = db.relationship("Website", backref="settings", lazy=True, uselist=True)

    @hybrid_property
    def running_time_from(self):
        return datetime.combine(self.from_date, self.from_time)

    @hybrid_property
    def running_time_to(self):
        return datetime.combine(self.to_date, self.to_time)

    def __repr__(self):
        return f"CTF('{self.ctf_name},'{self.organization_name}')"


# Websites Table


class Website(db.Model):
    __tablename__ = "website"
    id = db.Column(db.Integer, primary_key=True)
    settings_id = db.Column(
        db.Integer, db.ForeignKey("settings.id"), nullable=False, unique=False
    )
    url = db.Column(
        db.TEXT(), nullable=False, default="https://Abs0lut3Pwn4g3.github.io/"
    )
    name = db.Column(
        db.TEXT(), nullable=False, default="Official Abs0lut3Pwn4g3 Website"
    )

    def __repr__(self):
        return f"Website('{self.name}','{self.url}')"
