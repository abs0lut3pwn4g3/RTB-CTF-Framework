""" Helper functions """

import os
import secrets


def handle_secret_key():
    sk = os.environ.get("SECRET_KEY", None)
    if not sk:
        sk = secrets.token_hex(16)
        os.environ["SECRET_KEY"] = sk
    return sk


def handle_admin_pass():
    passwd = os.environ.get("ADMIN_PASS", None)
    if not passwd:
        passwd = secrets.token_hex(16)
        os.environ["ADMIN_PASS"] = passwd
    return passwd
