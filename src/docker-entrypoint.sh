#!/bin/sh

chmod +x init_db.sh runserver.sh
# init/ migrate DB
./init_db.sh
# run gunicorn production server
./runserver.sh