#!/bin/sh

export FLASK_APP="FlaskRTBCTF:create_app()"
exec gunicorn ${FLASK_APP} \
            --bind "0.0.0.0:8000" \
            --workers ${WORKERS:-4}
            --worker-class egg:meinheld#gunicorn_worker