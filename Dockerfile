FROM python:3

WORKDIR /usr/src/app
COPY src ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
RUN chown -R 1001:1001 .
USER 1001
RUN chmod +x /usr/src/app/docker-entrypoint.sh
ENTRYPOINT [ "/usr/src/app/docker-entrypoint.sh" ]