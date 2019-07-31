#!/bin/sh

WORKERS=4 # change here to the change number of workers

echo "Starting RTB-CTF-Framework"
exec gunicorn 'FlaskRTBCTF:create_app()' \
    --bind '0.0.0.0:8080' \
    --workers $WORKERS