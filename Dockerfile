FROM python:3

ENV SECRET_KEY="override-me"
ENV DEBUG="False"
ENV ALLOWED_HOSTS="*"

WORKDIR /code
COPY . /code/

RUN python setup.py install
RUN python manage.py collectstatic --noinput
RUN DISABLE_COLLECTSTATIC=1 python manage.py compress --force
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dvzo.wsgi", "--log-level", "debug"]
