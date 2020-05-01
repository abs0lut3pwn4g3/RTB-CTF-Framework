#!/bin/sh

python create_db.py
exec gunicorn "FlaskRTBCTF:create_app()" \
            --bind "0.0.0.0:8000" \
            --workers $WORKERS