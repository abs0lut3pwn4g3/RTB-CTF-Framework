from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TimeMixin(object):
    __mapper_args__ = {"always_refresh": True}

    updated_on = db.Column(
        db.TIMESTAMP(timezone=True),
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )


class ReprMixin(object):
    """Provides a string representible form for objects."""

    def __repr__(self):
        fields = {f: getattr(self, f, "<BLANK>") for f in self.__repr_fields__}
        pattern = ["{0}={{{0}}}".format(f) for f in self.__repr_fields__]
        pattern = ", ".join(pattern).format(**fields)
        return f"<{self.__class__.__name__}({pattern})>"
