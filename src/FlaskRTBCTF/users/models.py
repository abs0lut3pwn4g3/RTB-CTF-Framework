from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itertools import zip_longest

from flask import current_app
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from ..ctf.models import UserChallenge, Challenge, UserMachine, Machine
from ..utils.models import db
from ..utils.cache import cache
from ..utils.bcrypt import bcrypt
from ..utils.login_manager import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# User Model
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    email = db.Column(db.String(88), unique=True, nullable=False)
    _password = db.Column(db.String(64), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False)
    logs = db.relationship("Logs", backref="user", lazy=True, uselist=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        self._password = bcrypt.generate_password_hash(pwd).decode("utf-8")

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self.id}).decode("utf-8")

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except Exception:
            return None
        return User.query.get(user_id)

    @staticmethod
    @cache.cached(timeout=3600, key_prefix="users")
    def get_all():
        return User.query.all()

    @staticmethod
    @cache.memoize(timeout=3600 * 3)
    def points(id):
        challenge_ids = UserChallenge.completed_challenges(user_id=id)
        machine_ids = UserMachine.completed_machines(user_id=id)
        points = 0
        for idx in zip_longest(challenge_ids, machine_ids["user"], machine_ids["root"]):
            if idx[0]:
                points += (
                    Challenge.query.with_entities(Challenge.points)
                    .filter_by(id=idx[0])
                    .scalar()
                )
            if idx[1]:
                points += (
                    Machine.query.with_entities(Machine.user_points)
                    .filter_by(id=idx[1])
                    .scalar()
                )
            if idx[2]:
                points += (
                    Machine.query.with_entities(Machine.root_points)
                    .filter_by(id=idx[2])
                    .scalar()
                )
        return points

    def __repr__(self):
        return f"User('{self.username}', '{self.email}'))"


# User's Logs Model
class Logs(db.Model):
    __tablename__ = "logs"
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False, primary_key=True
    )
    accountCreationTime = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow()
    )
    visitedMachine = db.Column(db.Boolean, default=False)
    machineVisitTime = db.Column(db.DateTime, nullable=True)
    userSubmissionTime = db.Column(db.DateTime, nullable=True)
    rootSubmissionTime = db.Column(db.DateTime, nullable=True)
    userOwnTime = db.Column(db.String, nullable=True)
    rootOwnTime = db.Column(db.String, nullable=True)
    userSubmissionIP = db.Column(db.String, nullable=True)
    rootSubmissionIP = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"Logs('{self.user_id}', vistedMachine: '{self.visitedMachine}')"
