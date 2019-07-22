import datetime

from FlaskRTBCTF import create_app, db, bcrypt
from FlaskRTBCTF.models import User, Score, Notification
from FlaskRTBCTF.config import ctfname

app = create_app()

# create_app().app_context().push()
with app.app_context():
    db.create_all()

    # NOTE: CHANGE DEFAULT CREDENTIALS !!!
    admin_user = User(
        username='admin',
        email='admin@admin.com',
        password=bcrypt.generate_password_hash('admin').decode('utf-8'),
        confirmed_at=datetime.datetime.now(),
        isAdmin = True
    )
    score = Score(userid=admin_user.id, userHash=False, rootHash=False, score=0)
    notif = Notification(
        title=f"Welcome to {ctfname}",
        body = "The CTF is live now. Please read rules!"
    )
    db.session.add(admin_user)
    db.session.add(score)
    db.session.add(notif)
    db.session.commit()
