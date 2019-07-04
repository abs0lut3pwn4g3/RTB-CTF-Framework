''' Models '''

from FlaskRTBCTF import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    rank = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '#{self.rank}')"



