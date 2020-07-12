""" Helper functions """

import os
import secrets
from datetime import datetime

from flask import flash

from .cache import cache
from ..main.models import Settings, Website


def handle_admin_pass(default="admin"):
    passwd = os.environ.get("ADMIN_PASS", default)
    if not passwd:
        passwd = secrets.token_hex(16)
    return passwd


def handle_admin_email(default="admin@admin.com"):
    return os.environ.get("ADMIN_EMAIL", default)


def inject_app_context():
    settings = Settings.get_settings()
    websites = Website.get_websites()
    if settings.dummy:
        flash("Please setup the CTF by going to /setup.", "info")

    return dict(settings=settings, websites=websites)


def inject_security_headers(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    # response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


@cache.cached(timeout=60, key_prefix="past_running_time")
def is_past_running_time():
    end_date_time = Settings.get_settings().running_time_to
    current_date_time = datetime.utcnow()
    return current_date_time > end_date_time


def clear_points_cache(userId, mode):
    from ..ctf.models import UserChallenge, UserMachine
    from ..users.models import User

    cache.delete(key="scoreboard")
    if mode == "c":
        cache.delete_memoized(UserChallenge.completed_challenges, UserChallenge, userId)
    elif mode == "m":
        cache.delete_memoized(UserMachine.completed_machines, UserMachine, userId)
    cache.delete_memoized(User.points, userId)


def clear_rating_cache(user_id, ch_id=None, machine_id=None):
    from ..ctf.models import Machine, Challenge, UserChallenge, UserMachine

    if ch_id:
        cache.delete_memoized(Challenge.avg_rating, ch_id)
        cache.delete_memoized(UserChallenge.rated_challenges, UserChallenge, user_id)
    elif machine_id:
        cache.delete_memoized(Machine.avg_rating, machine_id)
        cache.delete_memoized(UserMachine.rated_machines, UserMachine, user_id)
    else:
        pass
