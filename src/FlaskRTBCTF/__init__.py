from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_mail import Mail
from FlaskRTBCTF.config import Config, LOGGING
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
admin_manager = Admin()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    admin_manager.init_app(app)
    # Add model views
    from FlaskRTBCTF.admin.views import MyModelView
    from FlaskRTBCTF.models import User, Score, Notification, Machine

    if LOGGING:
        from FlaskRTBCTF.models import Logs
    admin_manager.add_view(MyModelView(User, db.session))
    admin_manager.add_view(MyModelView(Score, db.session))
    admin_manager.add_view(MyModelView(Notification, db.session))
    admin_manager.add_view(MyModelView(Machine, db.session))
    if LOGGING:
        admin_manager.add_view(MyModelView(Logs, db.session))
    mail.init_app(app)

    from flask_sslify import SSLify

    # only trigger SSLify if the app is running on Heroku
    if "DYNO" in os.environ:
        _ = SSLify(app)

    from FlaskRTBCTF.users.routes import users
    from FlaskRTBCTF.ctf.routes import ctf
    from FlaskRTBCTF.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(ctf)
    app.register_blueprint(main)

    return app
