""" Helper functions """

import os
import secrets
from datetime import datetime

from .cache import cache
from FlaskRTBCTF.main.models import Settings, Website


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


def handle_admin_email(default="admin@admin.com"):
    em = os.environ.get("ADMIN_EMAIL", default)
    return em


def inject_app_context():
    settings = Settings.get_settings()
    websites = Website.get_websites()

    return dict(settings=settings, websites=websites)


@cache.cached(timeout=60, key_prefix="past_running_time")
def is_past_running_time():
    end_date_time = Settings.get_settings().running_time_to
    current_date_time = datetime.utcnow()
    return current_date_time > end_date_time
