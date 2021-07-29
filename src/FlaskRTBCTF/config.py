import os

# Flask related Configurations


class Config:
    DEBUG = False  # Turn DEBUG OFF before deployment
    SECRET_KEY = os.environ.get("SECRET_KEY", "you-will-never-guess")
    _uri = os.environ.get("DATABASE_URL") or "sqlite:///site.db"
    if _uri.startswith("postgres://"):
        _uri = _uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = _uri
    # For local use, one can simply use SQLlite with: 'sqlite:///site.db'
    # For deployment on Heroku use: `os.environ.get('DATABASE_URL')`
    # in all other cases: `os.environ.get('SQLALCHEMY_DATABASE_URI')`
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = ("journal", "paper", "yeti", "cosmo")[3]
    # TEMPLATES_AUTO_RELOAD = True
    # Session handling
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Strict"
    SESSION_COOKIE_SECURE = (
        True if os.environ.get("SSL_ENABLED", False) == "True" else False
    )
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
