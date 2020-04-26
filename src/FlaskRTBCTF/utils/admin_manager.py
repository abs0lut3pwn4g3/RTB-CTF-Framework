from flask_admin import Admin
from flask_admin.menu import MenuLink


admin_manager = Admin(template_mode="bootstrap3")
admin_manager.add_link(MenuLink(name="CTF Setup", url="/setup"))
admin_manager.add_link(MenuLink(name="Go Back", url="/"))
