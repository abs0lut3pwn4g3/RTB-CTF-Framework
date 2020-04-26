import os

from flask import Flask

from FlaskRTBCTF.config import Config
from FlaskRTBCTF.admin.views import BaseModelView, UserAdminView, MachineAdminView
from FlaskRTBCTF.utils import (
    db,
    bcrypt,
    login_manager,
    admin_manager,
    mail,
    inject_app_context,
)

from FlaskRTBCTF.users.models import User, Logs
from FlaskRTBCTF.main.models import Notification
from FlaskRTBCTF.ctf.models import Machine

from FlaskRTBCTF.users.routes import users
from FlaskRTBCTF.ctf.routes import ctf
from FlaskRTBCTF.main.routes import main

_blueprints = (users, ctf, main)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    admin_manager.init_app(app)
    mail.init_app(app)

    app.context_processor(inject_app_context)

    # Add model views for admin control
    admin_manager.add_view(UserAdminView(User, db.session))
    admin_manager.add_view(MachineAdminView(Machine, db.session))
    admin_manager.add_view(BaseModelView(Notification, db.session))
    admin_manager.add_view(BaseModelView(Logs, db.session))

    for _bp in _blueprints:
        app.register_blueprint(_bp)

    # only trigger SSLify if the app is running on Heroku
    if "DYNO" in os.environ:
        from flask_sslify import SSLify

        _ = SSLify(app)

    return app
