from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from FlaskRTBCTF.config import Config
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	from flask_sslify import SSLify
	if 'DYNO' in os.environ:  # only trigger SSLify if the app is running on Heroku
		sslify = SSLify(app)

	from FlaskRTBCTF.users.routes import users
	from FlaskRTBCTF.ctf.routes import ctf
	from FlaskRTBCTF.main.routes import main
	app.register_blueprint(users)
	app.register_blueprint(ctf)
	app.register_blueprint(main)

	return app