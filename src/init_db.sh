#!/bin/sh

flask db init
flask db migrate
flask db upgrade
python populate_db.prod.py
