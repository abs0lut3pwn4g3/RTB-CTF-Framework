import pytz
from datetime import datetime

from FlaskRTBCTF import db, create_app
from FlaskRTBCTF.main.models import Settings
from FlaskRTBCTF.ctf.models import Machine, Challenge, Tag, Category
from FlaskRTBCTF.users.models import User, Logs
from FlaskRTBCTF.utils.helpers import handle_admin_pass, handle_admin_email


app = create_app()


def populate_tags():
    db.session.add(Tag(label="web", color="#2B2B52"))
    db.session.add(Tag(label="pwn", color="#BB2CD9"))
    db.session.add(Tag(label="reversing", color="#218F76"))
    db.session.add(Tag(label="osint", color="#CB7303"))
    db.session.add(Tag(label="binary", color="#AE1438"))
    db.session.add(Tag(label="forensics", color="#2B2B52"))
    db.session.add(Tag(label="programming", color="#2B2B52"))


def populate_categories():
    category_names = [
        "binary",
        "web",
        "forensics",
        "steganography",
        "cryptography",
        "OSINT",
        "scripting",
        "networking",
        "misc",
    ]
    for name in category_names:
        db.session.add(Category(name=name))


def populate_websites():
    from FlaskRTBCTF.main.models import Website

    web1 = Website(
        name="Official Abs0lut3Pwn4g3 Website", url="https://Abs0lut3Pwn4g3.github.io/",
    )
    web2 = Website(name="Twitter", url="https://twitter.com/Abs0lut3Pwn4g3")
    web3 = Website(
        name="Source Code on GitHub",
        url="https://github.com/Abs0lut3Pwn4g3/RTB-CTF-Framework",
    )

    db.session.add(web1)
    db.session.add(web2)
    db.session.add(web3)


def populate_challs():
    box = Machine(
        name="Dummy Box. Edit/Delete this.",
        user_hash="A" * 32,
        root_hash="B" * 32,
        user_points=10,
        root_points=20,
        os="linux",
        ip="127.0.0.1",
        difficulty="easy",
    )
    db.session.add(box)

    ch1 = Challenge(
        title="Dummy challenge. Edit/Delete this.",
        description="blah blah",
        flag="CTF{test}",
        points="50",
        url="https://ch1.example.com/",
        difficulty="easy",
        category=Category.query.get(2),
        tags=[Tag.query.get(1), Tag.query.get(2)],
    )
    db.session.add(ch1)


with app.app_context():
    s = Settings.query.get(1)
    a = User.query.filter_by(username="admin").first()
    if s or a:
        print("populate_db.prod: Skipping since, database is already populated!")
        exit()

    now_time = datetime.now(pytz.utc)

    admin_user = User(
        username="admin",
        email=handle_admin_email(),
        password=handle_admin_pass(),
        isAdmin=True,
    )
    db.session.add(admin_user)

    admin_log = Logs(
        user=admin_user,
        accountCreationTime=now_time,
        visitedMachine=True,
        machineVisitTime=now_time,
    )
    db.session.add(admin_log)

    db.session.add(Settings(dummy=True))

    populate_tags()
    populate_categories()
    populate_websites()

    db.session.commit()

    populate_challs()

    print("populate_db.prod: Database populated with some default data!")

    db.session.commit()
