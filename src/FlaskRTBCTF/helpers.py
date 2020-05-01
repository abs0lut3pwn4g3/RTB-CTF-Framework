""" Helper functions """

import os
import secrets


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
