FROM python:3

WORKDIR /usr/src/app
COPY app ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
RUN chown -R 1001:1001 .
USER 1001
CMD gunicorn -w 4 -b 0.0.0.0:8080 run:"app:create_app()"