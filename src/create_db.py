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
    admin_score = Score(user=admin_user, userHash=False, rootHash=False, points=0)
    db.session.add(admin_user)
    db.session.add(admin_score)

    notif = Notification(
        title=f"Welcome to {ctfname}",
        body = "The CTF is live now. Please read rules!"
    )
    db.session.add(notif)

    '''    
    test = User(
        username='test',
        email='test@test.com',
        password=bcrypt.generate_password_hash('test').decode('utf-8'),
    )
    testscore = Score(user=test, userHash=False, rootHash=False, points=0)
    db.session.add(test)
    db.session.add(testscore)
    '''

    db.session.commit()
