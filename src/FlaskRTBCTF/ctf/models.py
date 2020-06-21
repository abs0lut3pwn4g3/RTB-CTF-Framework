from sqlalchemy.orm import joinedload
from sqlalchemy.sql import func

from FlaskRTBCTF.utils.models import db, TimeMixin, ReprMixin
from FlaskRTBCTF.utils.cache import cache


# Machine Table
class Machine(TimeMixin, ReprMixin, db.Model):
    __tablename__ = "machine"
    __repr_fields__ = (
        "name",
        "os",
    )
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    user_hash = db.Column(db.String(32), nullable=False)
    root_hash = db.Column(db.String(32), nullable=False)
    user_points = db.Column(db.Integer, default=0)
    root_points = db.Column(db.Integer, default=0)
    os = db.Column(db.String, nullable=False, default="linux")
    ip = db.Column(db.String(64), nullable=False)
    difficulty = db.Column(db.String, nullable=False, default="Easy")

    @staticmethod
    @cache.memoize(timeout=3600)
    def avg_rating(id):
        avg_rating = (
            UserMachine.query.with_entities(func.avg(UserMachine.rating))
            .filter(UserMachine.machine_id == id, UserMachine.rating != 0)
            .scalar()
        )
        return round(avg_rating, 1) if avg_rating else 0

    @staticmethod
    @cache.cached(timeout=3600 * 3, key_prefix="machines")
    def get_all():
        return Machine.query.all()


# UserMachine: N to N relationship
class UserMachine(TimeMixin, db.Model):
    __tablename__ = "user_machine"
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False,
        primary_key=True,
        index=True,
    )
    machine_id = db.Column(
        db.Integer,
        db.ForeignKey("machine.id"),
        nullable=False,
        primary_key=True,
        index=True,
    )
    owned_user = db.Column(db.Boolean, nullable=False, default=False)
    owned_root = db.Column(db.Boolean, nullable=False, default=False)
    rating = db.Column(db.Integer, nullable=False, default=0)

    @classmethod
    @cache.memoize(timeout=3600 * 3)
    def completed_machines(cls, user_id):
        completed = dict()
        _ids1 = (
            cls.query.with_entities(cls.machine_id)
            .filter_by(user_id=user_id, owned_user=True)
            .all()
        )
        _ids2 = (
            cls.query.with_entities(cls.machine_id)
            .filter_by(user_id=user_id, owned_root=True)
            .all()
        )
        completed["user"] = [int(id[0]) for id in _ids1]
        completed["root"] = [int(id[0]) for id in _ids2]
        return completed

    @classmethod
    @cache.memoize(timeout=3600 * 3)
    def rated_machines(cls, user_id):
        _ids = (
            cls.query.with_entities(cls.machine_id)
            .filter(cls.user_id == user_id, cls.rating != 0)
            .all()
        )
        _ids = [int(id[0]) for id in _ids]
        return _ids


# Tag Model
class Tag(ReprMixin, db.Model):
    __tablename__ = "tag"
    __repr_fields__ = ("label",)
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(32), nullable=False)
    color = db.Column(db.String(16), nullable=False)


# Tags table
tags = db.Table(
    "tags",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
    db.Column(
        "challenge_id", db.Integer, db.ForeignKey("challenge.id"), primary_key=True
    ),
)


# Challenges Model
class Challenge(TimeMixin, ReprMixin, db.Model):
    __tablename__ = "challenge"
    __repr_fields__ = ("title", "category")
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(64), nullable=False, unique=True)
    description = db.Column(db.TEXT, nullable=True)
    flag = db.Column(db.TEXT, nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)
    url = db.Column(db.TEXT, nullable=True)
    difficulty = db.Column(db.String, nullable=True)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", backref=db.backref("challenges", lazy=True))

    tags = db.relationship(
        "Tag",
        secondary=tags,
        lazy="subquery",
        backref=db.backref("challenges", lazy="noload"),
    )

    @staticmethod
    @cache.memoize(timeout=3600)
    def avg_rating(id):
        avg_rating = (
            UserChallenge.query.with_entities(func.avg(UserChallenge.rating))
            .filter(UserChallenge.challenge_id == id, UserChallenge.rating != 0)
            .scalar()
        )
        return round(avg_rating, 1) if avg_rating else 0


# UserChallenge: N to N relationship
class UserChallenge(TimeMixin, db.Model):
    __tablename__ = "user_challenge"
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False,
        primary_key=True,
        index=True,
    )
    challenge_id = db.Column(
        db.Integer,
        db.ForeignKey("challenge.id"),
        nullable=False,
        primary_key=True,
        index=True,
    )
    completed = db.Column(db.Boolean, nullable=False, default=False)
    rating = db.Column(db.Integer, nullable=False, default=0)

    @classmethod
    @cache.memoize(timeout=3600 * 3)
    def completed_challenges(cls, user_id):
        _ids = (
            cls.query.with_entities(cls.challenge_id)
            .filter_by(user_id=user_id, completed=True)
            .all()
        )
        _ids = [int(id[0]) for id in _ids]
        return _ids

    @classmethod
    @cache.memoize(timeout=3600 * 3)
    def rated_challenges(cls, user_id):
        _ids = (
            cls.query.with_entities(cls.challenge_id)
            .filter(cls.user_id == user_id, cls.rating != 0)
            .all()
        )
        _ids = [int(id[0]) for id in _ids]
        return _ids


# Category Model
class Category(ReprMixin, db.Model):
    __tablename__ = "category"
    __repr_fields__ = ("name",)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    @staticmethod
    @cache.cached(timeout=3600 * 3, key_prefix="challenges")
    def get_challenges():
        categories = (
            Category.query.options(joinedload("challenges"))
            .filter(Category.challenges)
            .all()
        )
        return categories
