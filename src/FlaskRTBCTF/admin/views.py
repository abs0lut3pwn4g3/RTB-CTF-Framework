""" Admin Model Views. """

from flask import abort, redirect, flash, url_for, request
from flask_login import current_user
from flask_admin import expose
from flask_admin.form import SecureForm
from flask_admin.contrib.sqla import ModelView

from ..utils.cache import cache
from ..utils.helpers import clear_points_cache


class BaseModelView(ModelView):
    export_types = ("csv", "json")
    can_export = True
    form_base_class = SecureForm
    column_display_pk = True  # optional, but I like to see the IDs in the list
    form_excluded_columns = ("created_on", "updated_on")

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
    can_view_details = True
    column_exclude_list = ("password",)
    form_exclude_list = ("password",)
    column_searchable_list = ("username", "email")

    @expose("/new/")
    def create_view(self):
        flash("Please use registration form for creating new users.", "info")
        return redirect("/admin/user")

    @staticmethod
    def after_model_delete(model):
        cache.delete(key="scoreboard")
        return


class MachineAdminView(BaseModelView):
    can_view_details = True
    column_searchable_list = ("name", "ip")

    @expose("/new/")
    def create_view(self):
        return redirect(url_for("ctf.new_machine"))

    @expose("/edit/")
    def edit_view(self):
        id = int(request.args["id"])
        return redirect(url_for("ctf.edit_machine", id=id))


class ChallengeAdminView(BaseModelView):
    can_view_details = True
    column_searchable_list = ("title", "url")
    form_choices = {
        "difficulty": [
            ("easy", "Easy"),
            ("medium", "Medium"),
            ("hard", "Hard"),
            ("insane", "Insane"),
        ]
    }

    @staticmethod
    def after_model_change(form, model, is_created):
        cache.delete(key="challenges")
        return

    @staticmethod
    def after_model_delete(model):
        cache.delete(key="challenges")
        return


class UserChallengeAdminView(BaseModelView):
    column_filters = ("completed",)
    column_list = ("user_id", "challenge_id", "completed")

    @staticmethod
    def after_model_change(form, model, is_created):
        if form.completed != model.completed:
            clear_points_cache(userId=model.user_id, mode="c")
        return

    @staticmethod
    def after_model_delete(model):
        clear_points_cache(userId=model.user_id, mode="c")
        return


class UserMachineAdminView(BaseModelView):
    column_filters = ("owned_user", "owned_root")
    column_list = ("user_id", "machine_id", "owned_user", "owned_root")

    @staticmethod
    def after_model_change(form, model, is_created):
        if (form.owned_user != model.owned_user) or (
            form.owned_root != model.owned_root
        ):
            clear_points_cache(userId=model.user_id, mode="m")
        return

    @staticmethod
    def after_model_delete(model):
        clear_points_cache(userId=model.user_id, mode="m")
        return


class NotificationAdminView(BaseModelView):
    column_searchable_list = ("title",)
