from datetime import datetime

from FlaskRTBCTF import create_app, db, bcrypt
from FlaskRTBCTF.models import User, Score, Notification, Machine
from FlaskRTBCTF.config import organization, LOGGING

if LOGGING:
    from FlaskRTBCTF.models import Logs

app = create_app()

# create_app().app_context().push()
with app.app_context():
    db.create_all()

    default_time = datetime.utcnow()
    
    box = Machine(
        name="My Awesome Pwnable Box",
        user_hash='A'*32,
        root_hash='B'*32,
        user_points=10,
        root_points=20,
        os="Linux",
        ip="127.0.0.1",
        hardness="You tell"
    )
    db.session.add(box)

    # NOTE: CHANGE DEFAULT CREDENTIALS !!!
    admin_user = User(
        username='admin',
        email='admin@admin.com',
        password=bcrypt.generate_password_hash('admin').decode('utf-8'),
        isAdmin=True
    )
    admin_score = Score(user=admin_user, userHash=False,
                        rootHash=False, points=0, machine=box)
    db.session.add(admin_user)
    db.session.add(admin_score)

    notif = Notification(
        title=f"Welcome to {organization['ctfname']}",
        body="The CTF is live now. Please read rules!"
    )
    db.session.add(notif)

    test_user = User(
        username='test',
        email='test@test.com',
        password=bcrypt.generate_password_hash('test').decode('utf-8')
    )
    test_score = Score(user=test_user, userHash=False,
                       rootHash=False, points=0, machine=box)
    db.session.add(test_user)
    db.session.add(test_score)

    if LOGGING:
        admin_log = Logs(user=admin_user, accountCreationTime=default_time,
                         visitedMachine=True, machineVisitTime=default_time)
        db.session.add(admin_log)
        test_log = Logs(user=test_user, accountCreationTime=default_time)
        db.session.add(test_log)

    db.session.commit()
