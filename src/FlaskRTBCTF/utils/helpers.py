""" Helper functions """

import os
import secrets
from datetime import datetime

from flask import request, redirect, url_for
from FlaskRTBCTF.main.models import Settings


def needs_setup():
    settings = Settings.query.get(1)
    if settings.dummy:
        if request.endpoint != "main.setup":
            return redirect(url_for("main.setup"))
    else:
        return


def handle_secret_key(default="you-will-never-guess"):
    sk = os.environ.get("SECRET_KEY", default)
    if not sk:
        sk = secrets.token_hex(16)
        os.environ["SECRET_KEY"] = sk
    return sk


def handle_admin_pass(default="admin"):
    passwd = os.environ.get("ADMIN_PASS", default)
    if not passwd:
        passwd = secrets.token_hex(16)
        os.environ["ADMIN_PASS"] = passwd
    return passwd


def inject_app_context():
    settings = Settings.query.get(1)
    # Note to self: maybe we can use? @cached_property:
    # https://werkzeug.palletsprojects.com/en/1.0.x/utils/#werkzeug.utils.cached_property

    return dict(settings=settings)


def is_past_running_time():
    end_date_time = Settings.query.get(1).running_time_to
    current_date_time = datetime.utcnow()
    return current_date_time > end_date_time
