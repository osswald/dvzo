import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path('.')

ENV_PATH = BASE_DIR / '.env'
load_dotenv(dotenv_path=ENV_PATH)

SECRET_KEY = os.getenv("SECRET_KEY")

if os.getenv("DEBUG") == "True":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS"), ]

PROJECT_APPS = [
    'train_management',
    'users'
]

INSTALLED_APPS = [
                     'whitenoise.runserver_nostatic',
                     'django.contrib.admin',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                     'django_tex',
                     'phonenumber_field',
                     'tapeforms',
                     'tinymce',
                     'compressor',
                 ] + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'users.User'

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

PHONENUMBER_DEFAULT_REGION = "CH"

ROOT_URLCONF = 'dvzo.urls'

TEMPLATE_DIR = BASE_DIR / 'templates'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'NAME': 'tex',
        'BACKEND': 'django_tex.engine.TeXEngine',
        'APP_DIRS': True,
    },
]

# django_tex resources
LATEX_INTERPRETER = 'pdflatex'
ASSET_DIR = BASE_DIR / 'static/assets'
LATEX_GRAPHICSPATH = [ASSET_DIR.as_posix()]

WSGI_APPLICATION = 'dvzo.wsgi.application'

if os.getenv("PRODUCTION") == "False":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USERNAME'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOSTNAME'),
            'PORT': os.getenv('DB_PORT'),
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'de-ch'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [BASE_DIR / 'templates/locale']

TINYMCE_JS_URL = 'https://cdn.tiny.cloud/1/mzzbdds45pytc0srczsext77st8du79k6rp4840guy0jdayk/tinymce/5/tinymce.min.js'
TINYMCE_COMPRESSOR = False
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link charmap preview anchor searchreplace visualblocks code "
               "fullscreen insertdatetime template table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontsizeselect formatselect | alignleft "
               "aligncenter alignright alignjustify | outdent indent | table | numlist bullist checklist | forecolor "
               "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
               "fullscreen | template link anchor | "
               "code",
    "custom_undo_redo_levels": 10,
    "templates": [
        {
            "title": "Abstellplanung",
            "description": "Fügt eine Tabelle für die Abstellplanung ein.",
            "content": "<h3>Parkordnung</h3><p>&nbsp;</p><table class='table table-striped table-sm'><tbody><tr>"
                       "<td style='background-color: #000000;'><strong><span style='color: #ecf0f1;'>Gleis</span>"
                       "</strong></td><td style='background-color: #000000;'><span style='color: #ecf0f1;'>"
                       "<strong>Belegung</strong></span></td></tr><tr><td>101</td>"
                       "<td>K3, K1, Hebamme, C107, BC, C6109, FZ203</td></tr><tr><td>102</td>"
                       "<td>Kohlewagen, L4/X402, Kranwagen, HoWa, FiWa, JaWa, F405, Olma</td></tr><tr><td>103</td>"
                       "<td>Dampfl&auml;deli, Bierwagen OK151, C105, WR109, C106, C4, F204</td></tr><tr><td>223</td>"
                       "<td>#16363, #354</td></tr><tr><td>224</td><td>P3 #4, P2 #9, P1 #2</td></tr><tr><td>225</td>"
                       "<td>P5 &amp; 6 C6075, P4 Shell</td></tr></tbody></table>",
        },
    ]
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "root": {"level": "INFO", "handlers": ["std_out"]},
    "handlers": {
        "std_out": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["std_out"],
            "level": "INFO",
            "propagate": True
        },
    },
    "formatters": {
        "app": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}
