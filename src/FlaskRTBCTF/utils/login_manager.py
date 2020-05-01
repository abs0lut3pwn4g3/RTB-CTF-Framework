from functools import wraps

from flask import flash, redirect
from flask_login import LoginManager, current_user


login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"


def admin_only(f):
    """
    Route decorator to require admin access.
    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user:
            if current_user.is_authenticated and current_user.isAdmin:
                return f(*args, **kwargs)
        flash("You are not authorized to perform this operation.", "danger")
        return redirect("/login")

    return decorated_function
