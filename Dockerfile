FROM python:3.8.2-alpine3.11

MAINTAINER eshaan7bansal@gmail.com

# Env
RUN export DATABASE_URL="postgres://${DB_USER}:${DB_PASSWORD}@postgres:${DB_PORT}/${DB_NAME}" \
    && export REDIS_URL="redis://redis:6379/0"

# update and install packages
RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base \
    && apk add --no-cache git libssl1.1 g++ make libffi-dev

# Add a new low-privileged user
RUN adduser --shell /sbin/login www-data -DH

# Install RTB-CTF-Framework
WORKDIR /usr/src/app
COPY src ./
RUN pip install --no-cache-dir -r requirements.txt \
    && chown -R www-data ./

USER www-data

EXPOSE 8000
RUN chmod +x /usr/src/app/docker-entrypoint.sh
ENTRYPOINT [ "/usr/src/app/docker-entrypoint.sh" ]