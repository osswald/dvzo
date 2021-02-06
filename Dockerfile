FROM python:3

WORKDIR /code
COPY . /code/
RUN python setup.py install
RUN python manage.py migrate

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dvzo.wsgi"]
