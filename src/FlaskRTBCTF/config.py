import os
from datetime import datetime
import pytz

''' Flask related Configurations. Note: DO NOT FORGET TO CHANGE SECRET_KEY ! '''

class Config:
    SECRET_KEY = 'you-will-never-guess' # os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    DEBUG = True # Turn DEBUG OFF before deployment
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

''' CTF related Configuration '''

# Specify CTF Name

ctfname = "RootTheBox CTF"

# Specify CTFs Running Time

RunningTime = { 
    "from": datetime(2019,7,7,15,00,00,0, pytz.timezone('Asia/Calcutta')), 
    "to": datetime(2019,7,8,0,00,00,0, pytz.timezone('Asia/Calcutta')), 
    "TimeZone": "IST"
} # Use `pytz.utc` for UTC timezone

# Speicfy Your Pwnable Box/Machine settings

box = { 
    "name": "My Awesome Pwnable Box", 
    "ip": "127.0.0.1", "os": 
    "Linux", 
    "points": { "user": 10, "root": 20 }, 
    "hardness": "You tell" 
}

# Specify The Hashes, you can use python's secrets package to generate them

userHash = 'A'*32 # dummy hash, length = 32 fixed
rootHash = 'B'*32 # dummy hash, length = 32 fixed
userScore = 10
rootScore = 20

# NOTE: CHANGE DEFAULT ADMIN CREDENTIALS in create_db.py !!!