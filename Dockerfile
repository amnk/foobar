FROM python:2-alpine3.6

EXPOSE 8080
VOLUME /usr/src/app/public
WORKDIR /usr/src/apps/foobar

RUN apk add --no-cache uwsgi uwsgi-python uwsgi-http

COPY foobar /usr/src/apps/foobar
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "uwsgi", "--plugin", "http,python", "--http", ":8080", "--wsgi-file", "wsgi.py", "--callable", "app", "--py-autoreload", "2"]
