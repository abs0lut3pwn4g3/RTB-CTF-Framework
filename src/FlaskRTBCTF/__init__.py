import os

from flask import Flask

from FlaskRTBCTF.config import Config
from FlaskRTBCTF.utils import (
    db,
    bcrypt,
    cache,
    login_manager,
    admin_manager,
    mail,
    inject_app_context,
)
from FlaskRTBCTF.users.routes import users
from FlaskRTBCTF.ctf.routes import ctf
from FlaskRTBCTF.main.routes import main


_blueprints = (users, ctf, main)

_extensions = (db, bcrypt, cache, login_manager, admin_manager, mail)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.context_processor(inject_app_context)

    for _ext in _extensions:
        _ext.init_app(app)

    for _bp in _blueprints:
        app.register_blueprint(_bp)

    # only trigger SSLify if the app is running on Heroku
    if "DYNO" in os.environ:
        from flask_sslify import SSLify

        _ = SSLify(app)

    return app
