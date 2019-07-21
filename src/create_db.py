import datetime

from FlaskRTBCTF import create_app, db, bcrypt
from FlaskRTBCTF.models import User, Score

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
    db.session.add(admin_user)
    db.session.add(score)
    db.session.commit()
