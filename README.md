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
python manage.py collectstatic --noinput  # only prod
python manage.py runserver
```

## Testing & Formatting

```
# install test dependencies
pip install ".[test]"

# run tests
python manage.py test
```

For the formatting we have flake8 and isort in place plus bandit for
vulnerability checks.

```
# run style checks (pep8)
flake8 .

# run isort checks (import sorting/ordering)
isort . [--check]

# check vulnerabilities
bandit --ini .bandit -r
```

## l10n

```
cd <APP>
django-admin makemessages -l de_CH
python manage.py compilemessages
```

## Resources

```
npm run dev  # bundle
npm install <package> --save  # install prod pkg
npm install <package --save-dev  # install dev pkg

npm run prod  # build resources for production
```

## Docker

```
# build image
docker build -t dvzo .
# create superuser inside the container
docker run -it dvzo:latest sh
# startup app
docker run -d -p 8000:8000 -e SECRET_KEY="secret" -e ALLOWED_HOSTS="*" dvzo:latest
```
