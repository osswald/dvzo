import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = 'dvzo'
VERSION = '0.1.0'
AUTHOR = 'osswald'
EMAIL = 'christoph.osswald@dvzo.ch'
DESCRIPTION = 'Betriebsplanung'
URL = 'https://github.com/osswald/dvzo'
REQUIRED = [
    'Pillow',
    'gunicorn',
    'django-compressor',
    'django_tex',
    'Django',
    'python-dotenv',
    'psycopg2-binary',
    'whitenoise[brotli]',
    'django-phonenumber-field[phonenumbers]',
    'django-tapeforms',
    'django-weasyprint',
    'Django'
]
TEST_REQUIRE = [
    'pytest',
    'pytest-azurepipelines',
    'flake8',
    'isort',
    'bandit',
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU GPL V3",
    ],
    install_requires=REQUIRED,
    extras_require={
        'test': TEST_REQUIRE
    },
)
