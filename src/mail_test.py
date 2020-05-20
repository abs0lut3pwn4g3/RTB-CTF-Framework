from flask import Blueprint
from flask_mail import Message
from FlaskRTBCTF import create_app,db
from FlaskRTBCTF.utils import mail
from FlaskRTBCTF.main.models import Settings , Website


app = create_app()

app.config['MAIL_PORT'] = 587
app.config['MAIL_DEFAULT_SENDER'] = ("Tester", "test@rtb.com")
app.config['DEBUG'] = True

    
with app.app_context():
    msg = Message("Hello",
        sender="from@example.com",
        recipients=["to@example.com"]
    )
    msg.body = "testing"
    mail.send(msg)