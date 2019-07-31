import os
from datetime import datetime
import pytz

''' Flask related Configurations. Note: DO NOT FORGET TO CHANGE SECRET_KEY ! '''

class Config:
    SECRET_KEY = 'you-will-never-guess' # os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # locally
    # If heroku use: `os.environ.get('DATABASE_URL')` 
    # in all other cases: `os.environ.get('SQLALCHEMY_DATABASE_URI')`
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    DEBUG = True # Turn DEBUG OFF before deployment
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

''' CTF related Configuration '''

# Add some information about organization and specify CTF name

organization = {
    "ctfname": "RootTheBox CTF",
    "name": "DEF CON 91120",
    "website": { 
        "url": "https://dc91120.org/",
        "name": "Official DC91120 Website"
    }, 
    "website_2": { 
        "url": "https://dc91120.org/events.html",
        "name": "Events"
    }, 
    "website_3": { 
        "url": "https://dc91120.org/#footer",
        "name": "About Us"
    }
}     

# Specify CTFs Running Time

RunningTime = { 
    "from": datetime(2019,7,7,15,00,00,0, pytz.utc), 
    "to": datetime(2019,7,8,0,00,00,0, pytz.utc), 
    "TimeZone": "UTC"
} # We do not recommended changing the Timezone.

# Specify Your Pwnable Box/Machine settings

box = { 
    "name": "My Awesome Pwnable Box", 
    "ip": "127.0.0.1", 
    "os": "Linux", 
    "points": { "user": 10, "root": 20 }, 
    "hardness": "You tell" 
}

# Specify The Hashes, you can use python's secrets package to generate them

userHash = 'A'*32 # dummy hash, length = 32 fixed
rootHash = 'B'*32 # dummy hash, length = 32 fixed
userScore = 10
rootScore = 20

# Logging: Set to 'True' to enable Logging in Admin Views.

LOGGING = True # We recommend to leave it on.

# NOTE: CHANGE DEFAULT ADMIN CREDENTIALS in create_db.py !!!
