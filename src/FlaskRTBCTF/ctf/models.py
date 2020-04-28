from FlaskRTBCTF.utils import db, cache

# Machine Table


class Machine(db.Model):
    __tablename__ = "machine"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    user_hash = db.Column(db.String(32), nullable=False)
    root_hash = db.Column(db.String(32), nullable=False)
    user_points = db.Column(db.Integer, default=0)
    root_points = db.Column(db.Integer, default=0)
    os = db.Column(db.String, nullable=False, default="linux")
    ip = db.Column(db.String(64), nullable=False)
    hardness = db.Column(db.String, nullable=False, default="Easy")

    @staticmethod
    @cache.cached(timeout=3600, key_prefix="machines")
    def get_all():
        _machines = Machine.query.all()
        return _machines
