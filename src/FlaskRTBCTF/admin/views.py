""" Admin Model Views. """

from flask import abort, redirect, flash, url_for, request
from flask_login import current_user
from flask_admin import expose
from flask_admin.form import SecureForm
from flask_admin.contrib.sqla import ModelView

from ..utils.cache import cache
from ..utils.helpers import clear_points_cache, clear_rating_cache


class BaseModelView(ModelView):
    can_view_details = True
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
    column_exclude_list = ("password", "_password")
    column_details_exclude_list = column_exclude_list
    column_descriptions = {
        "_password": """
        you can change the password here manually,
        it will be automatically hashed on save
        """,
        "isAdmin": "Think twice before checking this field.",
    }
    form_columns = ("username", "email", "isAdmin", "password")
    column_searchable_list = ("username", "email")

    @expose("/new/")
    def create_view(self):
        flash("Please use registration form for creating new users.", "info")
        return redirect("/admin/user")

    @staticmethod
    def after_model_delete(model):
        cache.delete(key="users")
        cache.delete(key="scoreboard")
        return


class MachineAdminView(BaseModelView):
    column_exclude_list = ("user_hash", "root_hash", "updated_on")
    column_searchable_list = ("name", "ip")
    column_filters = ("difficulty", "user_points", "root_points", "os")

    @expose("/new/")
    def create_view(self):
        return redirect(url_for("ctf.new_machine"))

    @expose("/edit/")
    def edit_view(self):
        id = int(request.args["id"])
        return redirect(url_for("ctf.edit_machine", id=id))


class ChallengeAdminView(BaseModelView):
    column_exclude_list = ("description", "flag", "url")
    column_searchable_list = ("title", "url", "flag")
    column_filters = ("difficulty", "points", "category")
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
    column_filters = ("completed", "user_id", "challenge_id")
    column_list = ("user_id", "challenge_id", "completed", "rating")
    form_choices = {
        "rating": [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]
    }

    @staticmethod
    def after_model_change(form, model, is_created):
        clear_points_cache(userId=model.user_id, mode="c")
        clear_rating_cache(user_id=model.user_id, ch_id=model.challenge_id)
        return

    @staticmethod
    def after_model_delete(model):
        clear_points_cache(userId=model.user_id, mode="c")
        clear_rating_cache(user_id=model.user_id, ch_id=model.challenge_id)
        return


class UserMachineAdminView(BaseModelView):
    column_filters = ("user_id", "machine_id", "owned_user", "owned_root", "rating")
    column_list = ("user_id", "machine_id", "owned_user", "owned_root", "rating")

    @staticmethod
    def after_model_change(form, model, is_created):
        clear_points_cache(userId=model.user_id, mode="m")
        clear_rating_cache(user_id=model.user_id, machine_id=model.machine_id)
        return

    @staticmethod
    def after_model_delete(model):
        clear_points_cache(userId=model.user_id, mode="m")
        clear_rating_cache(user_id=model.user_id, machine_id=model.machine_id)
        return


class NotificationAdminView(BaseModelView):
    column_searchable_list = ("title",)
