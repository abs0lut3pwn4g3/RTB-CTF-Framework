""" Admin Model Views. """

from flask import abort
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView


class MyModelView(ModelView):

    column_exclude_list = ("password",)

    def is_accessible(self):
        if not current_user.is_authenticated or not current_user.isAdmin:
            # permission denied
            abort(403)
        if current_user.isAdmin:
            return True
        return False

    def _handle_view(self, name, **kwargs):
        """ Override builtin _handle_view in order to redirect users when a
        view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
