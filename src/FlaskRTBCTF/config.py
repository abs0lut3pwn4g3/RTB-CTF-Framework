import os

class Config:
    SECRET_KEY = 'you-will-never-guess' # os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    DEBUG = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

ctfname = "RootTheBox CTF"
RunningTime = '{ "from": "3:00 PM 7th July 2019", "to": "12:00 AM 8th July 2019", "TimeZone": "IST" }'
box = '{ "name": "My Awesome Pwnable Box", "ip": "127.0.0.1", "os": "Linux", "points": { "user": 10, "root": 20 }, "hardness": "You tell" }'
userHash = 'A'*32 # dummy hash, length = 32 fixed
rootHash = 'B'*32 # dummy hash, length = 32 fixed
userScore = 10
rootScore = 20

'''
Creating site.db file
$ source venv/bin/activate
$ python3 # open python interpreter
>>> from FlaskRTBCTF import db, create_app
>>> db.create_all(app=create_app())
'''