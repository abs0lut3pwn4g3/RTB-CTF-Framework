import os

from .utils import handle_secret_key

# Flask related Configurations
# Note: DO NOT FORGET TO CHANGE 'SECRET_KEY' !


class Config:
    SECRET_KEY = handle_secret_key()
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///site.db"
    # For local use, one can simply use SQLlite with: 'sqlite:///site.db'
    # For deployment on Heroku use: `os.environ.get('DATABASE_URL')`
    # in all other cases: `os.environ.get('SQLALCHEMY_DATABASE_URI')`
    FLASK_ADMIN_SWATCH = ["journal", "paper", "yeti", "cosmo"][2]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False  # Turn DEBUG OFF before deployment
    # TEMPLATES_AUTO_RELOAD = True
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
