FROM python:3.8.3-alpine3.12

LABEL maintainer="eshaan7bansal@gmail.com"

# Env
RUN export DATABASE_URL="postgres://${DB_USER}:${DB_PASSWORD}@postgres:${DB_PORT}/${DB_NAME}" \
    && export REDIS_URL="redis://redis:6379/0"

# update and install packages
RUN apk update --no-cache \
    && apk add --no-cache postgresql-dev build-base g++ libffi-dev

# Add a new low-privileged user
RUN adduser --shell /sbin/login www-data -DH

# Install RTB-CTF-Framework
WORKDIR /usr/src/app
COPY src ./
RUN chown -R www-data ./
RUN pip install --no-cache-dir -r requirements.txt

USER www-data

EXPOSE 8000
RUN chmod +x /usr/src/app/docker-entrypoint.sh
ENTRYPOINT [ "/usr/src/app/docker-entrypoint.sh" ]