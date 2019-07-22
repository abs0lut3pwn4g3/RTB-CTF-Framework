''' Models '''

from flask import current_app
from FlaskRTBCTF import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

''' User Table '''

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    confirmed_at = db.Column(db.DateTime(), default=datetime.utcnow)
    isAdmin = db.Column(db.Boolean, default=False)
    score = db.relationship('Score', backref='user', lazy=True, uselist=False)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}') | Score('{self.score}')"


''' Score Table '''

class Score(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False, primary_key=True)
    userHash = db.Column(db.Boolean, default=False)
    rootHash = db.Column(db.Boolean, default=False)
    points = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"Score('{self.user_id}', '{self.points}')"


''' Notifications Table '''

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    body = db.Column(db.String(250), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Notif('{self.title}', '{self.body}')"
