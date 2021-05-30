FROM python:3.9.2-alpine3.13

ENV SECRET_KEY="override-me"
ENV DEBUG="False"
ENV ALLOWED_HOSTS="*"

# Update and install and bash
RUN apk update
RUN apk add --no-cache bash postgresql-libs
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg
RUN apk add --no-cache --virtual build-deps gcc python3-dev postgresql-dev musl-dev g++ gettext
RUN apk add --no-cache --update --virtual node nodejs npm
RUN apk add --no-cache --update gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

# Copy project
COPY . /home/dvzo/app

# Work Directory
WORKDIR /home/dvzo/app

# setup non-root user
RUN addgroup -S dvzo
RUN adduser -H -S dvzo -G dvzo -h /home/dvzo -s /bin/bash -u 1001
RUN chown dvzo:dvzo /home/dvzo -R
USER dvzo

# Install requirements
RUN python -m venv .venv
RUN .venv/bin/python -m pip install --upgrade pip
RUN .venv/bin/python setup.py install
RUN .venv/bin/python manage.py compilemessages
RUN npm i && npm run prod
RUN rm -rf node_modules
RUN .venv/bin/python manage.py collectstatic --noinput

RUN .venv/bin/python -m pip uninstall -y Pillow
RUN .venv/bin/python -m pip install Pillow

USER root
RUN apk --purge del build-deps
RUN apk --purge del node
USER dvzo

# Expose Port
EXPOSE 8000
CMD [".venv/bin/python", "-m", "gunicorn", "--bind", "0.0.0.0:8000", "dvzo.wsgi", "--log-level", "debug"]
