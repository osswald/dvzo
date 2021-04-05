# DVZO Betriebsplanung

## Beschreibung

Administrations-Software für die Planung und den Betrieb einer historischen Eisenbahn.
* Verwaltung von Fahrzeugen (Loks und Wagen)
* Verwaltung von Fahrtentagen mit einem oder mehreren Zügen (Komposition aus Fahrzeugen)
* Berechnung der Zuglast der Züge

## Installation and run

```
git clone git@github.com:osswald/dvzo.git
cd dvzo
python setup.py install
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## l10n

```
cd <APP>
django-admin makemessages -l de_CH
python manage.py compilemessages
```

## Docker

```
# build image
docker build -t dvzo --build-arg ADMIN_PW=secret .
# create superuser inside the container
docker run -it dvzo:latest sh
# startup app
docker run -d -p 8000:8000 dvzo:latest
```
