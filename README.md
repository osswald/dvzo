# DVZO Betriebsplanung

## Beschreibung

TODO

## Installation and run

### Requirements

- `pdflatex` for rendering the pdf files

### Getting started

```
git clone git@github.com:osswald/dvzo.git
cd dvzo
python setup.py install
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Docker

```
# build image
docker build -t dvzo --build-args ADMIN_PW=secret .
# create superuser inside the container
docker run -it dvzo:latest sh
# startup app
docker run -d -p 8000:8000 dvzo:latest
```
