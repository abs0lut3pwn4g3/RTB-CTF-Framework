#!/bin/sh

export FLASK_APP="FlaskRTBCTF:create_app()"
flask db init
flask db migrate
flask db upgrade
python populate_db.prod.py
