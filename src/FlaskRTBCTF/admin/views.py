""" Admin Model Views. """

from flask import abort, redirect, flash
from flask_login import current_user
from flask_admin import expose
from flask_admin.form import SecureForm
from flask_admin.contrib.sqla import ModelView


class BaseModelView(ModelView):
    export_types = ("csv", "json")
    can_export = True
    form_base_class = SecureForm

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


class UserAdminView(BaseModelView):
    column_exclude_list = ("password",)
    column_searchable_list = ("username", "email")

    @expose("/new/")
    def create_view(self):
        flash("Please use registration form for creating new users.", "info")
        return redirect("/admin/user")


class MachineAdminView(BaseModelView):
    column_searchable_list = ("name", "ip")
    form_choices = {
        "hardness": [("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")]
    }
