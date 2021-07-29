FROM python:3.9-alpine

LABEL maintainer="eshaan7bansal@gmail.com"

# Env
RUN export DATABASE_URL="postgresql://${DB_USER}:${DB_PASSWORD}@postgres:${DB_PORT}/${DB_NAME}" \
    && export REDIS_URL="redis://redis:6379/0"

# update and install packages
RUN apk update --no-cache \
    && apk add --no-cache postgresql-dev build-base g++ libffi-dev

# ensure www-data user exists (low-privileged user)
RUN set -x ; \
    addgroup -g 82 -S www-data ; \
    adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1

# Install RTB-CTF-Framework
WORKDIR /usr/src/app
COPY src ./
RUN chown -R www-data ./
RUN pip install --no-cache-dir -r requirements.txt

USER www-data

EXPOSE 8000
RUN chmod +x /usr/src/app/docker-entrypoint.sh
ENTRYPOINT [ "/usr/src/app/docker-entrypoint.sh" ]