# flake8: noqa
from .admin_manager import admin_manager
from .bcrypt import bcrypt
from .cache import cache
from .helpers import (
    handle_admin_pass,
    handle_admin_email,
    is_past_running_time,
    inject_app_context,
    inject_security_headers,
    clear_points_cache,
    clear_rating_cache,
)
from .login_manager import login_manager, admin_only
from .mail import mail, send_reset_email
from .models import db
from .minify import static_minify
from .migrate import migrate
