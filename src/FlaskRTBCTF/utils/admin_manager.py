from flask_admin import Admin
from flask_admin.menu import MenuLink

from FlaskRTBCTF.admin.views import (
    BaseModelView,
    UserAdminView,
    MachineAdminView,
    NotificationAdminView,
    ChallengeAdminView,
    UserChallengeAdminView,
    UserMachineAdminView,
)

from FlaskRTBCTF.users.models import User, Logs
from FlaskRTBCTF.main.models import Notification
from FlaskRTBCTF.ctf.models import (
    Machine,
    Challenge,
    Tag,
    Category,
    UserChallenge,
    UserMachine,
)
from .models import db

admin_manager = Admin(template_mode="bootstrap3")
admin_manager.add_link(MenuLink(name="CTF Setup", url="/setup"))
admin_manager.add_link(MenuLink(name="Go Back", url="/"))

# Add model views for admin control
admin_manager.add_view(NotificationAdminView(Notification, db.session))
admin_manager.add_view(UserAdminView(User, db.session, category="Users"))
admin_manager.add_view(BaseModelView(Logs, db.session, category="Users"))
admin_manager.add_view(ChallengeAdminView(Challenge, db.session, category="Challenges"))
admin_manager.add_view(
    UserChallengeAdminView(UserChallenge, db.session, category="Challenges")
)
admin_manager.add_view(BaseModelView(Category, db.session, category="Challenges"))
admin_manager.add_view(BaseModelView(Tag, db.session, category="Challenges"))
admin_manager.add_view(MachineAdminView(Machine, db.session, category="Machines"))
admin_manager.add_view(
    UserMachineAdminView(UserMachine, db.session, category="Machines")
)
