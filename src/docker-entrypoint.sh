#!/bin/sh

chmod +x init_db.sh runserver.sh
export FLASK_APP="FlaskRTBCTF:create_app()"
# init/ migrate DB
./init_db.sh
# run gunicorn production server
./runserver.sh